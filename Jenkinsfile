pipeline {
    agent any

    environment {
        DOCKER_IMAGE_NAME = "kanav2k03/myapp"           // Your Docker Hub repo
        DOCKERHUB_CREDENTIALS_ID = "dockerhub-pass"    // Jenkins credential ID (username + PAT)
        KUBE_DEPLOYMENT_NAME = "myapp"                 // Kubernetes deployment name
        KUBE_NAMESPACE = "default"                     // Kubernetes namespace
    }

    stages {
        stage('1. Checkout Code') {
            steps {
                echo 'Checking out code...'
                // Explicitly clone repo to avoid "not in a git directory"
                git branch: 'main', url: 'https://github.com/kanav03/Devops_PBL3.git'
            }
        }

        stage('2. Build Docker Image') {
            steps {
                echo "Building Docker image: ${DOCKER_IMAGE_NAME}"

                // Ensure Docker can be used (needed if Jenkins runs in a container)
                sh '''
                if [ ! -S /var/run/docker.sock ]; then
                    echo "Docker socket not found! Exiting..."
                    exit 1
                fi
                '''

                // Tag image with build number and 'latest'
                sh "docker build -t ${DOCKER_IMAGE_NAME}:${env.BUILD_NUMBER} ."
                sh "docker tag ${DOCKER_IMAGE_NAME}:${env.BUILD_NUMBER} ${DOCKER_IMAGE_NAME}:latest"
            }
        }

        stage('3. Push Image to Docker Hub') {
            steps {
                echo "Logging in and pushing image to Docker Hub..."
                withCredentials([usernamePassword(credentialsId: DOCKERHUB_CREDENTIALS_ID, usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh "echo \$DOCKER_PASS | docker login -u \$DOCKER_USER --password-stdin"
                    sh "docker push ${DOCKER_IMAGE_NAME}:${env.BUILD_NUMBER}"
                    sh "docker push ${DOCKER_IMAGE_NAME}:latest"
                    sh "docker logout"
                }
            }
        }

        stage('4. Deploy to Kubernetes') {
            steps {
                echo "Deploying to Kubernetes..."
                sh "kubectl set image deployment/${KUBE_DEPLOYMENT_NAME} ${KUBE_DEPLOYMENT_NAME}=${DOCKER_IMAGE_NAME}:${env.BUILD_NUMBER} -n ${KUBE_NAMESPACE}"
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
