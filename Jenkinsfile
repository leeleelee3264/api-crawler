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

        script {
          env.GIT_COMMIT_MSG = sh(script: 'git log -1 --pretty=%B ${GIT_COMMIT}', returnStdout: true).trim()
          env.GIT_COMMIT_AUTHOR = sh(script: 'git log -1 --pretty=format:%an ${GIT_COMMIT}', returnStdout: true).trim()
          env.GIT_COMMIT_SHORT = sh(script: 'git log -1 --pretty=%h ${GIT_COMMIT}', returnStdout: true).trim()
        }
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
      notiBuilder('Success', DEPLOY_TAG)
    }

    unstable {
      notiBuilder('Unstable', DEPLOY_TAG)
    }

    failure {
      notiBuilder('Failed', DEPLOY_TAG)
    }
  }
}

def notiBuilder(String status, String deploy) {

  if (deploy == 'yes') {
    message = ':fire: *Deploy* result :fire:'
  } else {
    message = ':fire: *Build* result :fire:'
  }

  if (status == 'Success') {
    url = "https://user-images.githubusercontent.com/35620531/229273784-65b4130d-f346-461d-8b81-bf900c8c4348.png"
  } else if (status == 'Unstable') {
    url = "https://user-images.githubusercontent.com/35620531/229323315-e5097666-b75b-4c4d-97f6-65cd4c56d53e.png"
  } else {
    url = "https://user-images.githubusercontent.com/35620531/229273778-1f7c720f-2e4b-4440-8fa0-11924b93978e.png"
  }

  def githubUrl = env.GIT_URL
  def urlWithoutGit = githubUrl.replaceAll(/\.git$/, '') + '/commit/' + env.GIT_COMMIT_SHORT

  def blocks = [
    [
      "type": "section",
      "text": [
        "type": "mrkdwn",
        "text": message
      ],
      "accessory": [
        "type": "button",
        "text": [
          "type": "plain_text",
          "text": "Github",
          "emoji": true
        ],
        "value": "click_me_123",
        "url": urlWithoutGit,
        "action_id": "button-action"
      ]
    ],
    [
      "type": "section",
      "text": [
        "type": "mrkdwn",
        "text": "Your Jenkins result is.... ${status}!"
      ],
      "accessory": [
        "type": "image",
        "image_url": url,
        "alt_text": "status"
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
          "text": "*Author*\n${env.GIT_COMMIT_AUTHOR}"
        ],
        [
          "type": "mrkdwn",
          "text": "*Builder Number*\n${env.BUILD_NUMBER}"
        ],
        [
          "type": "mrkdwn",
          "text": "*Commit*\n${env.GIT_COMMIT_SHORT}"
        ],
        [
          "type": "mrkdwn",
          "text": "*Commit Message*\n${env.GIT_COMMIT_MSG}"
        ]
      ]
    ],
    [
      "type": "divider"
    ],
  ]

  slackSend(
    channel: "#my-jenkins",
    blocks: blocks,
    unfurl_links: false
  )
}