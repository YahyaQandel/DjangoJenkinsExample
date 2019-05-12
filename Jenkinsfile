pipeline {
    agent any
    stages {
        stage('Preparing') {
            steps {
                echo "Running tests"
            }
        }
        stage('Tests') {
            steps {

                sh 'python manage.py test'
            }
        }
    }
}