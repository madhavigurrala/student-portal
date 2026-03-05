pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                echo "Cloning GitHub Repository..."
                git branch: 'main', url: 'https://github.com/madhavigurrala/student-portal.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                echo "Installing Flask..."
                bat 'pip install flask'
            }
        }

        stage('Run Application') {
            steps {
                echo "Running Flask App..."
                bat 'python app.py'
            }
        }

    }
}
