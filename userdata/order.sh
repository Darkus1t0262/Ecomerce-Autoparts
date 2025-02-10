#!/bin/bash
sudo yum update -y
sudo yum install docker -y
sudo service docker start
sudo docker run -d -p 5000:5000 --name order-service darkjus/order-service:latest
