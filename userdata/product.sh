#!/bin/bash
sudo yum update -y
sudo yum install docker -y
sudo service docker start
sudo docker run -d -p 4000:4000 --name product-service darkjus/product-service:latest
