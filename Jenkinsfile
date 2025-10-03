pipeline {
    agent any

    environment {
        DOCKER_IMAGE_NAME = "kanav2003/myapp"               // Your Docker Hub repo
        DOCKERHUB_CREDENTIALS_ID = "dockerhub-pass"        // Jenkins credential ID (username + PAT)
        KUBE_DEPLOYMENT_NAME = "myapp"                     // Kubernetes deployment name
        KUBE_NAMESPACE = "default"                         // Kubernetes namespace
    }

    stages {
        stage('1. Checkout Code') {
            steps {
                echo 'Checking out code...'
                checkout scm
            }
        }

        stage('2. Build Docker Image') {
            steps {
                echo "Building Docker image: ${DOCKER_IMAGE_NAME}"
                // Tag image with build number and 'latest'
                sh "docker build -t ${DOCKER_IMAGE_NAME}:${env.BUILD_NUMBER} ."
                sh "docker tag ${DOCKER_IMAGE_NAME}:${env.BUILD_NUMBER} ${DOCKER_IMAGE_NAME}:latest"
            }
        }

        stage('3. Push Image to Docker Hub') {
            steps {
                echo "Logging in and pushing image to Docker Hub..."
                // Use Jenkins credentials securely
                withCredentials([usernamePassword(credentialsId: DOCKERHUB_CREDENTIALS_ID, usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    // Secure Docker login
                    sh "echo \$DOCKER_PASS | docker login -u \$DOCKER_USER --password-stdin"
                    // Push both tags
                    sh "docker push ${DOCKER_IMAGE_NAME}:${env.BUILD_NUMBER}"
                    sh "docker push ${DOCKER_IMAGE_NAME}:latest"
                    sh "docker logout"
                }
            }
        }

        stage('4. Deploy to Kubernetes') {
            steps {
                echo "Deploying to Kubernetes..."
                // Update the deployment image dynamically to use the new build
                sh "kubectl set image deployment/${KUBE_DEPLOYMENT_NAME} ${KUBE_DEPLOYMENT_NAME}=${DOCKER_IMAGE_NAME}:${env.BUILD_NUMBER} -n ${KUBE_NAMESPACE}"
                // Wait for rollout to complete
                sh "kubectl rollout status deployment/${KUBE_DEPLOYMENT_NAME} -n ${KUBE_NAMESPACE}"
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished.'
        }
        success {
            echo "Build and deployment succeeded!"
        }
        failure {
            echo "Pipeline failed. Check logs above for details."
        }
    }
}
