pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-creds')
        PATH = "/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/Applications/Docker.app/Contents/Resources/bin:/opt/homebrew/bin:${env.PATH}"
    }

    triggers {
        githubPush()  
    }

    stages {
        stage('Checkout') {
            steps {
                script {
                    echo "Cloning the repository..."
                    git branch: 'main',
                        url: 'https://github.com/Anujesh-Ansh/Note_App-Flexi.git'
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    echo "Building Docker image..."
                    sh 'docker build -t anujeshansh/notesapp:latest .'
                }
            }
        }

        stage('Login to DockerHub') {
            steps {
                script {
                    echo "Logging in to DockerHub..."
                    withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DOCKERHUB_USER', passwordVariable: 'DOCKERHUB_PASSWORD')]) {
                        sh '''
                        echo $DOCKERHUB_PASSWORD | docker login -u $DOCKERHUB_USER --password-stdin
                        '''
                    }
                }
            }
        }

        stage('Run Tests with Pytest') {
            steps {
                script {
                    echo "Running tests with pytest and generating XML report..."
                    sh 'docker run --rm -v $(pwd):/app -w /app -e PYTHONPATH=/app 21070122022/notesapp:latest pytest tests --junitxml=result.xml'
                }
            }
        }

        stage('Archive Test Results') {
            steps {
                script {
                    echo "Archiving pytest results..."
                    archiveArtifacts artifacts: 'result.xml'
                }
            }
        }

        stage('Push Test Results to GitHub') {
            steps {
                script {
                    echo "Pushing result.xml to GitHub..."
                    sh '''
                    git config --global user.email "youremail@example.com"
                    git config --global user.name "Your Name"
                    git add result.xml
                    git commit -m "Add pytest results"
                    git push origin main
                    '''
                }
            }
        }

        stage('Push Docker Image to DockerHub') {
            steps {
                script {
                    echo "Pushing Docker image to DockerHub..."
                    sh 'docker push 21070122022/notesapp:latest'
                }
            }
        }

        stage('Logout from DockerHub') {
            steps {
                script {
                    echo "Logging out from DockerHub..."
                    sh 'docker logout'
                }
            }
        }
    }

    post {
        always {
            echo "Cleaning up the workspace..."
            cleanWs()  
        }
        failure {
            echo 'Build failed!'
        }
        success {
            echo 'Build succeeded!'
        }
    }
}
