pipeline {
    agent any
    stages {
        stage('Preparing') {
            steps {
                echo "installing python packages"
                sh "python --version"
                sh "sudo apt-get install python-pip"
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