pipeline {
    agent any

    environment {
        DOCKER_IMAGE_NAME      = "kanav2k03/myapp"
        DOCKERHUB_CREDENTIALS_ID = "dockerhub-pass"
    }

    stages {
        stage('1. Checkout Code') {
            steps {
                // This is the standard checkout step that reads from the job configuration.
                checkout scm
            }
        }

        stage('2. Build Docker Image') {
            steps {
                echo "Building Docker image: ${DOCKER_IMAGE_NAME}"
                sh "docker build -t ${DOCKER_IMAGE_NAME}:${env.BUILD_NUMBER} ."
                sh "docker tag ${DOCKER_IMAGE_NAME}:${env.BUILD_NUMBER} ${DOCKER_IMAGE_NAME}:latest"
            }
        }

        stage('3. Push Image to Docker Hub') {
            steps {
                echo "Logging in and pushing image to Docker Hub..."
                withCredentials([usernamePassword(credentialsId: DOCKERHUB_CREDENTIALS_ID, usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh "docker login -u ${DOCKER_USER} -p ${DOCKER_PASS}"
                    sh "docker push ${DOCKER_IMAGE_NAME}:${env.BUILD_NUMBER}"
                    sh "docker push ${DOCKER_IMAGE_NAME}:latest"
                    sh "docker logout"
                }
            }
        }

        stage('4. Deploy to Kubernetes') {
            steps {
                echo 'Deploying to Kubernetes...'
                // Use the correct hostname that matches the TLS certificate
                sh 'kubectl --server=https://kubernetes.docker.internal:6443 apply -f deployment.yaml'
                sh 'kubectl --server=https://kubernetes.docker.internal:6443 apply -f service.yaml'
                sh 'kubectl --server=https://kubernetes.docker.internal:6443 rollout restart deployment/myapp'
            }
        }
    }

    post {
        always {
            // Clean up the workspace after every build
            deleteDir()
            echo 'Pipeline finished.'
        }
    }
}
