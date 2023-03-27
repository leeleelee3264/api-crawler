pipeline {
  agent any

  stages {
    stage('Checkout') {
      steps {
        sh "git branch -D ${env.BRANCH_NAME}" // Delete existing branch
        git branch: "${env.BRANCH_NAME}",
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
        echo "INFO: Deploy: this is master only"
      }
    }
    post {
      success {
       slackSend color: 'good', message: "Build successful!"
      }
      failure {
       slackSend color: 'danger', message: "Build failed :cry:"
      }
    }
  }
}
