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
