pipeline {
    agent any

    environment {
        GITHUB_CREDENTIALS = credentials('github-creds')  // GitHub credentials
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-creds')  // DockerHub credentials
        DOCKER_IMAGE = '21070122001/notesapp'  // Replace with your Docker Hub repository
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout the latest code from GitHub
                git url: 'https://github.com/aadityaahire7/Notesweb_01.git',
                    credentialsId: GITHUB_CREDENTIALS,
                    branch: 'main'  // Use your main branch here
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image using the Dockerfile in the repository
                    docker.build("${DOCKER_IMAGE}:latest", ".")  // Assuming your Dockerfile is in the root
                }
            }
        }

        stage('Push to DockerHub') {
            steps {
                script {
                    // Push the built Docker image to Docker Hub
                    docker.withRegistry('https://index.docker.io/v1/', DOCKERHUB_CREDENTIALS) {
                        docker.image("${DOCKER_IMAGE}:latest").push()
                    }
                }
            }
        }
    }

    post {
        always {
            cleanWs() // Clean workspace after every build
        }

        success {
            echo 'Build succeeded! Docker image pushed to Docker Hub.'
        }

        failure {
            echo 'Build failed!'
        }
    }
}
