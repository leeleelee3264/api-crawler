pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git branch: 'master',
                    credentialsId: 'github_access_token',
                    url: 'https://github.com/leeleelee3264/musical-twitterbot-without-selenium.git'
            }
        }
    }

        post {
        success {
            slackSend (
                channel: '#jenkins-cicd',
                color: '#00FF00',
                message: "SUCCESS!!"
            )
        }
        failure {
            slackSend (
                channel: '#jenkins-cicd',
                color: '#FF0000',
                message: "FAIL!!"
            )
        }
    }
}