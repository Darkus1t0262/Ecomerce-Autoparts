#!/bin/bash
sudo yum update -y
sudo yum install docker -y
sudo service docker start
sudo docker run -d -p 5000:5000 --name order-service darkjus/order-service:latest
export MONGO_URI="mongodb://admin:password@mongo-db:27017/products_db?authSource=admin"
echo "✅ MongoDB URI set in environment."

# Start the service (Example command, replace as needed)
node server.js
