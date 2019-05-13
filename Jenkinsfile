pipeline {
    agent any
    stages {
        stage('Preparing') {
            steps {
                echo "installing python packages"
                sh "python --version"
                sh "easy_install pip"
            }
        }
        stage('Installing dependencies') {
            steps {
                sh "pip install -r requirements.txt"
            }
        }
        stage('Tests') {
            steps {

                sh 'python manage.py test'
            }
        }
    }
}