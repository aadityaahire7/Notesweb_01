#!/bin/bash

# Update and install Docker
sudo yum update -y
sudo amazon-linux-extras install docker -y
sudo service docker start

# Pull and run the notesapp Docker image
sudo docker pull 21070122001/notesapp:latest
sudo docker run -p 5000:5000 21070122001/notesapp:latest

# Install Java (required for ELK stack)
sudo yum install java-1.8.0-openjdk.x86_64 -y

# Install Elasticsearch
sudo rpm --import https://artifacts.elastic.co/GPG-KEY-elasticsearch
sudo tee /etc/yum.repos.d/elasticsearch.repo <<EOF
[elasticsearch]
name=Elasticsearch repository for 7.x packages
baseurl=https://artifacts.elastic.co/packages/7.x/yum
gpgcheck=1
gpgkey=https://artifacts.elastic.co/GPG-KEY-elasticsearch
enabled=1
autorefresh=1
type=rpm-md
EOF
sudo yum install elasticsearch -y
sudo systemctl start elasticsearch
sudo systemctl enable elasticsearch

# Install Logstash
sudo yum install logstash -y
sudo systemctl start logstash
sudo systemctl enable logstash

# Install Kibana
sudo yum install kibana -y
sudo systemctl start kibana
sudo systemctl enable kibana

# Configure firewall to allow Kibana and Elasticsearch
sudo firewall-cmd --permanent --add-port=5601/tcp   # Kibana
sudo firewall-cmd --permanent --add-port=9200/tcp   # Elasticsearch
sudo firewall-cmd --reload

# Print completion message
echo "ELK Stack and Docker application setup completed!"
