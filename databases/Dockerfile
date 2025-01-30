# Use official MongoDB image
FROM mongo:6

# Set environment variables for default admin user
ENV MONGO_INITDB_ROOT_USERNAME=admin
ENV MONGO_INITDB_ROOT_PASSWORD=password

# Copy initialization script to the container
COPY mongo-init.js /docker-entrypoint-initdb.d/

# Expose MongoDB default port
EXPOSE 27017

# Run MongoDB as the main process
CMD ["mongod"]
