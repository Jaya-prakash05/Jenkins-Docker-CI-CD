 
pipeline {
    agent any

    environment {
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
                    credentialsId: 'dockerhub-new',
                    usernameVariable: 'DH_USER',
                    passwordVariable: 'DH_PASS'
                )]) {
                    sh '''
                        echo "$DH_PASS" | docker login -u "$DH_USER" --password-stdin
                        docker tag myapp:latest $IMAGE_NAME:latest
                        docker push $IMAGE_NAME:latest
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
            echo 'Pipeline Failed !'
        }
    }
}
