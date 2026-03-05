pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                echo "Cloning Repository..."
                git branch: 'main', url: 'https://github.com/madhavigurrala/student-portal.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '"C:\\Users\\GURRALA MADHAVI\\AppData\\Local\\Programs\\Python\\Python314\\python.exe" -m pip install flask'
            }
        }

        stage('Run Application') {
            steps {
                bat '"C:\\Users\\GURRALA MADHAVI\\AppData\\Local\\Programs\\Python\\Python314\\python.exe" app.py'
            }
        }

    }
}
