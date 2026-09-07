pipeline {
    agent any

    stages {

        stage('Build') {
            steps {
                echo 'Building the application...'
                sh 'python3 -m compileall app'
            }
        }

        stage('Test') {
            steps {
                echo 'Running application tests...'
                sh 'python3 -m unittest discover -s app'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application...'

                sh '''
                    mkdir -p /tmp/devops-lab-1-deployed
                    cp app/app.py /tmp/devops-lab-1-deployed/app.py

                    if [ -f /tmp/devops-lab-1.pid ]; then
                        kill $(cat /tmp/devops-lab-1.pid) 2>/dev/null || true
                    fi

                    nohup python3 /tmp/devops-lab-1-deployed/app.py \
                        > /tmp/devops-lab-1.log 2>&1 &

                    echo $! > /tmp/devops-lab-1.pid
                '''
            }
        }
    }

    post {
        success {
            echo 'CI/CD pipeline completed successfully!'
        }

        failure {
            echo 'CI/CD pipeline failed.'
        }
    }
}
