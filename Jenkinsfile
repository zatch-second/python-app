pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Database preperation'){
            steps{
                sh 'docker compose up -d db'
                sleep 5
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    python3 -m venv venv
                    source venv/bin/activate
                    pip install -r requirements.txt
                    pytest test_app.py --junitxml=report.xml
                '''
            }
            post {
                always {
                    // This tells Jenkins to look for the file and build the UI graph
                    junit 'report.xml'
                }
            }
        }

        stage('Cleanup'){
            steps{
                sh 'docker compose down'
            }
        }
    }
}