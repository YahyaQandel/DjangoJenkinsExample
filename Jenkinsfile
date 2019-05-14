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
        stage('Installing dependencies') {
            steps {
             sh "export PATH=$PATH:/usr/local/bin && pip --version"
            }
        }
        stage('Tests') {
            steps {
                sh '/usr/local/bin/pip install -r requirements.txt '
                sh 'python manage.py test'
            }
        }
    }
}