pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-creds')
        GITHUB_CREDENTIALS = credentials('github-creds') // Add your GitHub credentials
        // Add Docker's path
        PATH = "/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/Applications/Docker.app/Contents/Resources/bin:/opt/homebrew/bin:${env.PATH}"
    }

    triggers {
        githubPush()  // Trigger on push to GitHub
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
                    // Build the Docker image with your Docker Hub tag
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

        stage('Push Docker Image to DockerHub') {
            steps {
                script {
                    echo "Pushing Docker image to DockerHub..."
                    // Push the Docker image to DockerHub
                    sh 'docker push anujeshansh/notesapp:latest'
                }
            }
        }

        // SonarQube Analysis Stage
        stage('SonarQube Analysis') {
            steps {
                script {
                    // Ensure SonarQube Scanner is available in Jenkins
                    def scannerHome = tool 'SonarQube Scanner'
                    withSonarQubeEnv('SonarQube') {
                        sh "${scannerHome}/bin/sonar-scanner -Dsonar.projectKey=note_app-flexi -Dsonar.projectName=note_app-flexi"
                    }
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    echo "Running tests..."
                    sh '''
                    # Create virtual environment and activate it
                    python -m venv venv
                    source venv/bin/activate

                    # Install dependencies
                    pip install -r requirements.txt
                    pip install pytest pytest-xml

                    # Run tests and generate result.xml
                    pytest tests/test_simple.py --junitxml=result.xml
                    '''
                }
            }
        }
        
        stage('Archive Test Results') {
            steps {
                script {
                    echo "Archiving test results..."
                    archiveArtifacts artifacts: 'result.xml', allowEmptyArchive: true
                    junit 'result.xml'
                }
            }
        }

        stage('Commit and Push Test Results') {
            steps {
                script {
                    echo "Committing and pushing test results..."
                    withCredentials([usernamePassword(credentialsId: 'github-creds', usernameVariable: 'GITHUB_USER', passwordVariable: 'GITHUB_PASSWORD')]) {
                        sh '''
                        git config --global user.email "anujesh.ansh.btech2021@sitpune.edu.in"
                        git config --global user.name "Anujesh-Ansh"

                        # Add result.xml to git
                        git add result.xml

                        # Commit the changes
                        git commit -m "Add test results"

                        # Push the changes
                        git push https://$GITHUB_USER:$GITHUB_PASSWORD@github.com/Anujesh-Ansh/Note_App-Flexi.git main
                        '''
                    }
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
