#!/bin/bash
sudo yum update -y
sudo amazon-linux-extras install docker -y
sudo service docker start
sudo docker pull 21070122001/notesapp:latest
sudo docker run -p 5000:5000 21070122001/notesapp:latest
