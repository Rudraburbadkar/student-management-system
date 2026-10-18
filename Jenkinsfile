
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Build') {
            steps {
                echo 'Building Student Management System'
            }
        }

        stage('Test') {
            steps {
                bat 'python -m pytest -v'
            }
        }
    }
}
