pipeline{
    agent any
    stages {
        stage(checkout code){
            steps{
                checkout scm
            }    
        }
        stage(run code){
            steps{
                sh 'python3 test_app.py'
            }
        }
    }
}