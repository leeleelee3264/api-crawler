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
                def blocks = [
                    [
                        "type": "section",
                        "text": [
                            "type": "mrkdwn",
                            "text": "Hello, Assistant to the Regional Manager Dwight! *Michael Scott* wants to know where you'd like to take the Paper Company investors to dinner tonight.\n\n *Please select a restaurant:*"
                        ]
                    ],
                    [
                        "type": "divider"
                    ],
                    [
                        "type": "section",
                        "text": [
                            "type": "mrkdwn",
                            "text": "*Farmhouse Thai Cuisine*\n:star::star::star::star: 1528 reviews\n They do have some vegan options, like the roti and curry, plus they have a ton of salad stuff and noodles can be ordered without meat!! They have something for everyone here"
                        ]
                    ]
                ]

                if (DEPLOY_TAG == 'yes') {
                    slackSend (
                        channel: '#jenkins-cicd',
                        color: '#00FF00',
                        message: "SUCCESS With Deploy!!",
                        blocks: blocks
                    )
                } else {
                    slackSend (
                        channel: '#jenkins-cicd',
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
                            "text": "*Pipeline Failed*\nOh no! Something went wrong and the pipeline failed. Please check the logs for more information."
                        ]
                    ]
                ]

                slackSend (
                    channel: '#jenkins-cicd',
                    color: '#FF0000',
                    message: "FAILURE!!",
                    blocks: blocks
                )
            }
        }
    }
}