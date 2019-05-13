pipeline {
    agent { docker { image 'python:3.7.2' } }
    stages {
        stage('Preparing') {
            steps {
                echo "installing python packages"
                sh "python --version"
                sh "sudo easy_install pip"
                sh "export PATH=$PATH:/usr/local/bin"
            }
        }
        stage('Installing dependencies') {
            steps {
                sh "pip --version"
            }
        }
        stage('Tests') {
            steps {
                sh 'python manage.py test'
            }
        }
    }
}