#!/bin/bash

# Update and install Docker
sudo yum update -y
sudo amazon-linux-extras install docker -y
sudo service docker start

# Pull and run the notesapp Docker image
sudo docker pull 21070122001/notesapp:latest
sudo docker run -d -p 5000:5000 21070122001/notesapp:latest

# Pull Elasticsearch, Logstash, and Kibana Docker images
sudo docker pull docker.elastic.co/elasticsearch/elasticsearch:7.10.0
sudo docker pull docker.elastic.co/logstash/logstash:7.10.0
sudo docker pull docker.elastic.co/kibana/kibana:7.10.0

# Run Elasticsearch container
sudo docker run -d --name elasticsearch -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:7.10.0

# Run Logstash container
sudo docker run -d --name logstash -p 5044:5044 -p 9600:9600 docker.elastic.co/logstash/logstash:7.10.0

# Run Kibana container
sudo docker run -d --name kibana -p 5601:5601 --link elasticsearch:elasticsearch docker.elastic.co/kibana/kibana:7.10.0

# Print completion message
echo "Docker containers for notesapp, Elasticsearch, Logstash, and Kibana are running."
