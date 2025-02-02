mongo-db:
  image: mongo:latest
  container_name: mongo-db
  restart: always
  networks:
    - backend
  ports:
    - "27017:27017"
  environment:
    - MONGO_INITDB_ROOT_USERNAME=admin
    - MONGO_INITDB_ROOT_PASSWORD=password
  volumes:
    - mongo-data:/data/db
    - ./mongo-init.js:/docker-entrypoint-initdb.d/mongo-init.js:ro
  healthcheck:
    test: ["CMD", "mongosh", "--eval", "db.adminCommand('ping').ok"]
    interval: 10s
    retries: 5
    start_period: 10s
