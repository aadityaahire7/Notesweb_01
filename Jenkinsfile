pipeline {
    agent any

    environment {
        // Use the correct DockerHub and AWS credentials IDs from your Jenkins
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-creds')
        AWS_ACCESS_KEYS = credentials('IAM_AWS')  // AWS credentials
        PATH="C:\Program Files\terraform_1.9.8_windows_amd64\terraform.exe"
    }

    triggers {
        githubPush()  // Automatically triggers the pipeline on a push to the GitHub repo
    }

    stages {
        stage('Checkout') {
            steps {
                script {
                    // Checkout code from the GitHub repository
                    git branch: 'main', url: 'https://github.com/aadityaahire7/Notesweb_01.git'
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image with the tag notesapp:latest
                    bat 'docker build -t "21070122001/notesapp:latest" .'
                }
            }
        }

        stage('Login to DockerHub') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DOCKERHUB_USER', passwordVariable: 'DOCKERHUB_PASSWORD')]) {
                        // Login to Docker Hub
                        bat 'docker login -u %DOCKERHUB_USER% -p %DOCKERHUB_PASSWORD%'
                    }
                }
            }
        }

        stage('Push Docker Image to DockerHub') {
            steps {
                script {
                    // Push the notesapp:latest image to Docker Hub
                    bat 'docker push 21070122001/notesapp:latest'
                }
            }
        }

        stage('Terraform Init') {
            steps {
                script {
                    // Change directory to the terraform folder
                    dir('terraform') {
                        // Initialize Terraform
                        bat 'terraform init'
                    }
                }
            }
        }

        stage('Terraform Plan') {
            steps {
                script {
                    // Change directory to the terraform folder
                    dir('terraform') {
                        // Run Terraform Plan
                        bat 'terraform plan'
                    }
                }
            }
        }

        stage('Terraform Apply') {
            steps {
                script {
                    // Change directory to the terraform folder
                    dir('terraform') {
                        // Apply Terraform changes
                        bat 'terraform apply -auto-approve'
                    }
                }
            }
        }

        stage('Logout from DockerHub') {
            steps {
                script {
                    // Logout from Docker Hub
                    bat 'docker logout'
                }
            }
        }
    }

    post {
        always {
            script {
                // Clean the workspace after the pipeline run
                cleanWs()
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
