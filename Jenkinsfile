pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-creds')
    }

    triggers {
        githubPush()  // Trigger on push to GitHub
    }

    stages {
        stage('Checkout') {
            steps {
                script {
                    git branch: 'main',
                        url: 'https://github.com/Anujesh-Ansh/Note_App-Flexi.git'
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image with your Docker Hub tag
                    sh 'docker build -t 21070122022/notesapp:latest .'
                }
            }
        }

        stage('Login to DockerHub') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DOCKERHUB_USER', passwordVariable: 'DOCKERHUB_PASSWORD')]) {
                        sh '''
                        echo $DOCKERHUB_PASSWORD | docker login -u $DOCKERHUB_USER --password-stdin
                        '''
                    }
                }
            }
        }

        stage('Push Docker Image to DockerHub') {
            steps {
                script {
                    // Push the Docker image to DockerHub
                    sh 'docker push 21070122022/notesapp:latest'
                }
            }
        }

        stage('Logout from DockerHub') {
            steps {
                script {
                    sh 'docker logout'
                }
            }
        }
    }

    post {
        always {
            cleanWs()  // Clean workspace after the build
        }
        failure {
            echo 'Build failed!'
        }
        success {
            echo 'Build succeeded!'
        }
    }
}
