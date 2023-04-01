def getBuildUser() {
    return currentBuild.rawBuild.getCause(Cause.UserIdCause).getUserId()
}

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
        always {
            script {
                BUILD_USER = getBuildUser()
                def commitInfo = sh(script: 'git log --pretty=format:"%h - %an: %s" -1', returnStdout: true).trim()
                def commitUrl = sh(script: 'git log --pretty=format:"https://github.com/leeleelee3264/musical-twitterbot-without-selenium/commit/%H" -1', returnStdout: true).trim()
            }
        }
        success {
            script {
                def blocks = [
                    [
                        "type": "section",
                        "text": [
                            "type": "mrkdwn",
                            "text": "*This is CI/CD result from Jenkins*"
                        ]
                    ],
                    [
                        "type": "divider"
                    ],
                    [
                        "type": "section",
                        "fields": [
                            [
                                "type": "mrkdwn",
                                "text": "*Status*\n${currentBuild.currentResult}"
                            ],
                            [
                                "type": "mrkdwn",
                                "text": "*Branch*\n${env.BRANCH_NAME}"
                            ],
                            [
                                "type": "mrkdwn",
                                "text": "*Output*\n<${env.BUILD_URL}|${env.JOB_NAME}#${env.BUILD_NUMBER}>"
                            ],
                            [
                                "type": "mrkdwn",
                                "text": "*Author*\n${BUILD_USER}"
                            ],
                            [
                                "type": "mrkdwn",
                                "text": "*Builder Number*\n${env.BUILD_NUMBER}"
                            ],
                            [
                                "type": "mrkdwn",
                                "text": "*Commit*\n${commitUrl}"
                            ],
                            [
                                "type": "mrkdwn",
                                "text": "*Commit Message*\n${commitInfo}"
                            ]
                        ]
                    ]
                ]

                if (DEPLOY_TAG == 'yes') {
                    slackSend (
                        channel: '#my-jenkins',
                        color: '#00FF00',
                        message: "SUCCESS With Deploy!!",
                        blocks: blocks
                    )
                } else {
                    slackSend (
                        channel: '#my-jenkins',
                        color: '#00FF00',
                        message: "SUCCESS!!",
                        blocks: blocks
                    )
                }
            }
        }

        failure {
            script {
                def blocks = [
                    [
                        "type": "section",
                        "text": [
                            "type": "mrkdwn",
                            "text": "*Build Result*"
                        ]
                    ],
                    [
                        "type": "divider"
                    ],
                    [
                        "type": "section",
                        "fields": [
                            [
                                "type": "mrkdwn",
                                "text": "*Status*\n${currentBuild.currentResult}"
                            ],
                            [
                                "type": "mrkdwn",
                                "text": "*Branch*\n${env.BRANCH_NAME}"
                            ],
                            [
                                "type": "mrkdwn",
                                "text": "*Output*\n<${env.BUILD_URL}|${env.JOB_NAME}#${env.BUILD_NUMBER}>"
                            ],
                            [
                                "type": "mrkdwn",
                                "text": "*Author*\n${BUILD_USER}"
                            ],
                            [
                                "type": "mrkdwn",
                                "text": "*Builder Number*\n${env.BUILD_NUMBER}"
                            ],
                            [
                                "type": "mrkdwn",
                                "text": "*Commit*\n<htts://github.com|frewr32>"
                            ],
                            [
                                "type": "mrkdwn",
                                "text": "*Commit Message*\nThis is commit message. long long long long long long"
                            ]
                        ]
                    ]
                    ]
                }
            }
        }
}