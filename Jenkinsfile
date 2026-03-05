pipeline {
agent any

```
environment {
    PYTHON = "python"
}

stages {

    stage('Checkout Code') {
        steps {
            echo "Cloning GitHub Repository..."
            git branch: 'main', url: 'https://github.com/madhavigurrala/student-portal.git'
        }
    }

    stage('Install Dependencies') {
        steps {
            echo "Installing Python dependencies..."
            bat '''
            python -m venv venv
            venv\\Scripts\\activate
            pip install flask
            '''
        }
    }

    stage('Run Application') {
        steps {
            echo "Starting Flask Application..."
            bat '''
            venv\\Scripts\\activate
            python app.py
            '''
        }
    }

    stage('Build Complete') {
        steps {
            echo "Pipeline executed successfully!"
        }
    }
}
```

}
