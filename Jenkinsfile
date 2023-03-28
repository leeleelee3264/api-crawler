pipeline {
    agent any
    environment {
        DEPLOY_TAG = 'no'
    }

    stages {
        stage('Clone') {
            steps {
                git branch: env.BRANCH_NAME,
                credentialsId: 'github_access_token',
                url: 'https://github.com/leeleelee3264/musical-twitterbot-without-selenium.git'
            }
        }
        stage('Build') {
            steps {
                echo "INFO: Build"
            }
        }
        stage('Integration') {
            steps {
                echo "INFO: Integration"
            }
        }
        stage('Test') {
            steps {
                echo "INFO: Test"
            }
        }
        stage('Deploy') {
            when {
                branch 'master'
            }
            steps {
                script {
                    DEPLOY_TAG = 'yes'
                }
                echo "INFO: Deploy: this is master only"
            }
        }
    }

    post {
        success {
            script {
                if (DEPLOY_TAG == 'yes') {
                    slackSend (
                        channel: '#jenkins-cicd',
                        color: '#00FF00',
                        message: "SUCCESS With Deploy!!"
                    )
                } else {
                    slackSend (
                        channel: '#jenkins-cicd',
                        color: '#00FF00',
                        message: "SUCCESS!!"
                    )
                }
            }
        }
        failure {
            script {
                if (DEPLOY_TAG == 'yes') {
                    slackSend (
                        channel: '#jenkins-cicd',
                        color: '#00FF00',
                        message: "Failed With Deploy!!"
                    )
                } else {
                    slackSend (
                        channel: '#jenkins-cicd',
                        color: '#00FF00',
                        message: "Failed!!"
                    )
                }
            }
        }
    }
}