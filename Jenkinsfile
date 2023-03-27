pipeline {
  agent any

  stages {
    stage('Checkout') {
      when {
        allOf {
         branch 'master'
         expression { env.BRANCH_NAME ==~ /^pull\/.*$/ }
        }
      }
      steps {
        sh "git branch -D ${env.BRANCH_NAME}" // Delete existing branch
        git branch: "${env.BRANCH_NAME}",
        credentialsId: 'github_access_token',
        url: 'https://github.com/leeleelee3264/musical-twitterbot-without-selenium.git'
      }
    }
    stage('Build') {
      when {
        allOf {
         branch 'master'
         expression { env.BRANCH_NAME ==~ /^pull\/.*$/ }
        }
      }
      steps {
        echo "INFO: Build"
      }
    }
    stage('Integration') {
      when {
        allOf {
         branch 'master'
         expression { env.BRANCH_NAME ==~ /^pull\/.*$/ }
        }
      }
      steps {
        echo "INFO: Integration"
      }
    }
    stage('Test') {
      when {
        allOf {
         branch 'master'
         expression { env.BRANCH_NAME ==~ /^pull\/.*$/ }
        }
      }
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