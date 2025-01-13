import os

# Define the list of microservices and their folder names
microservices = [
    "auth_service",
    "product_catalog_service",
    "inventory_service",
    "rental_service",
    "payment_gateway_service",
    "notification_service",
    "admin_panel_service",
    "analytics_service",
    "search_service",
    "reviews_service",
    "recommendation_service",
    "pricing_service",
    "chat_support_service",
    "logging_service",
    "shipping_service",
    "graph_api_service",
    "cache_service",
    "load_testing_service",
    "backup_service",
]

# Define the base structure for each microservice
base_structure = [
    "src",               # Source code
    "tests",             # Unit tests
    "docs",              # Documentation
    "config",            # Configuration files
    "Dockerfile",        # Dockerfile for containerization
    "README.md",         # Readme for the microservice
    "requirements.txt",  # Dependency file for Python (can be adjusted for other languages)
]

# Base directory where all microservices will be created
base_dir = "project_microservices"

# Generate the folder structure
for service in microservices:
    service_dir = os.path.join(base_dir, service)
    os.makedirs(service_dir, exist_ok=True)

    for item in base_structure:
        item_path = os.path.join(service_dir, item)

        # Create directories for src, tests, docs, and config
        if item in ["src", "tests", "docs", "config"]:
            os.makedirs(item_path, exist_ok=True)
        else:
            # Create empty files for Dockerfile, README.md, requirements.txt
            open(item_path, "w").close()

print(f"Microservices folder structure created in '{base_dir}'")
