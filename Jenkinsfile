pipeline {
    agent { 
        node {
            label 'docker-agent-python'
            }
      }
    triggers {
        // Poll the Git repository every 5 minutes
        pollSCM('H/5 * * * *')
    }
    
    }
    stages {
        stage('Build') {
            steps {
                echo "Building.."
                sh '''
                python3 jenkins.py
                '''
            }
        }
        stage('Test') {
            steps {
                echo "Testing.."
                sh '''
                echo "doing test stuff.."
                
                '''
            }
        }
        stage('Deliver') {
            steps {
                echo 'Deliver....'
                sh '''
                echo "doing delivery stuff.."
                '''
            }
        }
    }
}
