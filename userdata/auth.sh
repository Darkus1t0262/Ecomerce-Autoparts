#!/bin/bash
sudo yum update -y
sudo yum install docker -y
sudo service docker start
sudo docker run -d -p 3000:3000 --name auth-service darkjus/auth-service:latest
