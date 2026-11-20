pipeline {
    agent any

    environment {
        DOCKER_USER = 'jayaprakash5'
        IMAGE_NAME = 'jayaprakash5/myapp'
    }

    stages {

        stage('GitHub') {
            steps {
                git branch: 'main',
            url: 'https://github.com/Jaya-prakash05/Jenkins-Docker-CI-CD.git'
            }
        }

        stage('Build') {
            steps {
                sh 'docker build -t myapp .'
            }
        }

        stage('Push') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKER_USERNAME',
                    passwordVariable: 'DOCKER_PASSWORD'
                )]) {
                    sh '''
                        echo "$DOCKER_PASSWORD" | docker login \
                        -u "$DOCKER_USERNAME" --password-stdin

                        docker tag myapp:latest $IMAGE_NAME:latest

                        docker push $IMAGE_NAME:latest

                        docker logout
                    '''
                }
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                    docker pull $IMAGE_NAME:latest

                    docker rm -f myapp || true

                    docker run -d \
                    --name myapp \
                    --restart unless-stopped \
                    -p 5000:5000 \
                    $IMAGE_NAME:latest
                '''
            }
        }
    }

    post {
        success {
            echo 'Deployment Successful!'
        }

        failure {
            echo 'Pipeline Failed!'
        }
    }
}
