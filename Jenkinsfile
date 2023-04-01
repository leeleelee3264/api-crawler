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
            notiBuilder('Success', 'good', DEPLOY_TAG)
        }

        failure {
            notiBuilder('Failed', 'danger', DEPLOY_TAG)
        }
    }
}


def notiBuilder(String status, String colorCode, String deploy) {

  if (deploy == 'yes') {
    message = ':fire: *Deploy* result :fire:'
  } else {
    message = ':fire: *Build* result :fire:'
  }

  def blocks = [
    [
      "type": "section",
      "text": [
        "type": "mrkdwn",
        "text": message
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
          "text": "*Status*\n${status}"
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
          "text": "*Author*\n"
        ],
        [
          "type": "mrkdwn",
          "text": "*Builder Number*\n${env.BUILD_NUMBER}"
        ],
        [
          "type": "mrkdwn",
          "text": "*Commit*\nwww"
        ],
        [
          "type": "mrkdwn",
          "text": "*Commit Message*\nwww"
        ]
      ]
    ],
    [
      "type": "divider"
    ]
  ]

  slackSend (
    channel: '#my-jenkins',
    color: colorCode,
    blocks: blocks
  )
}