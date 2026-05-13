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

        stage('Install Playwright Browsers') {
            steps {
                bat 'python -m playwright install chromium'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'python -m pytest --headed --video=on --output=test-results --junit-xml=test-results/results.xml -v'
            }
        }
    }

    post {
        always {
            junit testResults: 'test-results/results.xml', allowEmptyResults: true
            archiveArtifacts artifacts: 'test-results/**/*', allowEmptyArchive: true
        }
        success {
            echo 'All tests passed!'
        }
        failure {
            echo 'Tests failed. Check archived videos in test-results/.'
        }
    }
}
