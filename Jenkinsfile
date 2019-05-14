pipeline {
    agent any
    stages {
        stage('Preparing') {
            steps {
                echo "installing python packages"
                sh "python --version"
                sh "sudo easy_install pip"

            }
        }
        stage('Tests') {
            steps {
                sh sudo /usr/local/bin/pip install -r requirements.txt '
                sh 'python manage.py test'
            }
        }
    }
}