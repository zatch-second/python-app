pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Run Tests') {
            steps {
                sh 'python3 test_app.py'
            }
        }
        
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t jenkins-python-app:latest .'
            }
        }
    }
}