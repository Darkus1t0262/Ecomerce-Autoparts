#!/bin/bash
sudo yum update -y
sudo yum install docker -y
sudo service docker start
sudo docker run -d -p 6000:6000 --name inventory-service darkjus/inventory-service:latest
