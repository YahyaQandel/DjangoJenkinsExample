pipeline {
    agent any
    stages {
        stage('Preparing') {
            steps {
                echo "installing python packages"
                sh "python --version"
                sh "sudo easy_install pip"
                sh "export PATH=$PATH:/usr/local/bin"
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