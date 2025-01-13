import os

# Define the root directory for the project
root_dir = 'final_project_structure'

# Define the structure
structure = {
    "microservices": {
        "user_authentication": ["app.py", "Dockerfile"],
        "product_management": ["app.py", "Dockerfile"],
        "payment_processing": ["app.py", "Dockerfile"],
        "notification_system": ["app.py", "Dockerfile"],
        "order_management": ["app.py", "Dockerfile"],
        # Add more services as needed
    },
    "frontend": {
        "src": ["App.js"],
        "": ["package.json"]
    },
    "infrastructure": {
        "terraform": [
            "mysql_rds.tf", 
            "dynamodb.tf", 
            "mongodb_ec2.tf", 
            "redis_elasticache.tf"
        ],
        "": ["docker-compose.yml", "prometheus_grafana_compose.yml"]
    },
    "backup": {
        "": ["backup_to_s3.sh"]
    },
    ".github": {
        "workflows": ["ecs_deployment_workflow.yml"]
    },
    "": ["README.md"]
}

# Create the directory structure
for folder, content in structure.items():
    base_path = os.path.join(root_dir, folder)
    os.makedirs(base_path, exist_ok=True)
    if isinstance(content, dict):  # Nested directories
        for subfolder, files in content.items():
            subfolder_path = os.path.join(base_path, subfolder)
            os.makedirs(subfolder_path, exist_ok=True)
            for file_name in files:
                open(os.path.join(subfolder_path, file_name), 'w').close()  # Create empty file
    else:  # Files in the current folder
        for file_name in content:
            open(os.path.join(base_path, file_name), 'w').close()  # Create empty file

print(f"Project structure created at: {os.path.abspath(root_dir)}")
