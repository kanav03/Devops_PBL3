pipeline {
    // Run this pipeline on any available Jenkins agent
    agent any

    // Define environment variables for the whole pipeline
    environment {
        DOCKER_IMAGE_NAME      = "kanav2003/myapp"
        DOCKERHUB_CREDENTIALS_ID = "dockerhub-pass" // The ID of the credential you created in Jenkins
    }

    stages {
        stage('1. Checkout Code') {
            steps {
                // This fetches the source code from your Git repository
                echo 'Checking out code...'
                checkout scm
            }
        }

        stage('2. Build Docker Image') {
            steps {
                echo "Building Docker image: ${DOCKER_IMAGE_NAME}"
                // We tag the image with both the unique build number and 'latest'
                // This is a best practice for versioning
                sh "docker build -t ${DOCKER_IMAGE_NAME}:${env.BUILD_NUMBER} ."
                sh "docker tag ${DOCKER_IMAGE_NAME}:${env.BUILD_NUMBER} ${DOCKER_IMAGE_NAME}:latest"
            }
        }

        stage('3. Push Image to Docker Hub') {
            steps {
                echo "Logging in and pushing image to Docker Hub..."
                // Use Jenkins's built-in credential manager for security
                withCredentials([usernamePassword(credentialsId: DOCKERHUB_CREDENTIALS_ID, usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh "docker login -u ${DOCKER_USER} -p ${DOCKER_PASS}"
                    // Push both tags to the registry
                    sh "docker push ${DOCKER_IMAGE_NAME}:${env.BUILD_NUMBER}"
                    sh "docker push ${DOCKER_IMAGE_NAME}:latest"
                    sh "docker logout"
                }
            }
        }

        stage('4. Deploy to Kubernetes') {
            steps {
                echo 'Deploying to Kubernetes...'
                // Apply the updated configurations to your cluster
                sh 'kubectl apply -f deployment.yaml'
                sh 'kubectl apply -f service.yaml'
                // Force a restart of the deployment to ensure it pulls the new 'latest' image
                sh 'kubectl rollout restart deployment/myapp'
            }
        }
    }

    post {
        // This block will always run at the end of the pipeline, regardless of status
        always {
            echo 'Pipeline finished.'
        }
    }
}