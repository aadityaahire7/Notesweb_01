pipeline {
    agent any

    environment {
        // Use the correct DockerHub credential ID from your Jenkins
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-creds')
    }

    triggers {
        githubPush()  // Automatically triggers the pipeline when a push is made to the GitHub repo
    }

    stages {
        stage('Checkout') {
            steps {
                script {
                    git branch: 'main',
                        url: 'https://github.com/aadityaahire7/Notesweb_01.git'
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image with your Docker Hub tag
                    bat 'docker build -t "21070122001/notesapp:latest" .'
                }
            }
        }

        stage('Login to DockerHub') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DOCKERHUB_USER', passwordVariable: 'DOCKERHUB_PASSWORD')]) {
                        bat '''
                        docker login -u %DOCKERHUB_USER% -p %DOCKERHUB_PASSWORD%
                        '''
                    }
                }
            }
        }

        stage('Push Docker Image to DockerHub') {
            steps {
                script {
                    // Push the Docker image to DockerHub
                    bat 'docker push 21070122001/notesapp:latest'
                }
            }
        }

        stage('Logout from DockerHub') {
            steps {
                script {
                    bat 'docker logout'
                }
            }
        }
    }

    post {
        always {
            script {
                // Clean the workspace after the pipeline run
                node {
                    cleanWs()
                }
            }
        }
        failure {
            echo 'Build failed!'
        }
        success {
            echo 'Build succeeded!'
        }
    }
}
