Errors that i faced during this project
Error :  docker not found in Jenkins build stage    Solution : Entered Jenkins container as root and installed Docker
apt update 
apt install -y docker.io
Error : Permission denied while accessing /var/run/docker.sock Solution : Added jenkins user to the docker group
usermod -aG docker jenkins
docker restart jenkins-docker
Error : Still permission denied? Fixed it with  Solution : chmod 666 /var/run/docker.sock

