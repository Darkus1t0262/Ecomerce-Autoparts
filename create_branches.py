import os
import subprocess

# List of microservice names
microservices = [
    "user-service",
    "product-service",
    "order-service",
    "payment-service",
    "notification-service",
    "inventory-service",
    "review-service",
    "auth-service",
    "shipping-service",
    "reporting-service",
    "analytics-service",
    "graphql-service",
    "websocket-service",
    "rpc-service",
    "soap-service",
    "cache-service",
    "search-service",
    "admin-service",
    "logging-service",
    "monitoring-service"
]

# Function to execute shell commands
def run_command(command):
    try:
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {' '.join(command)}")
        print(e.stderr)

# Create and push branches
for service in microservices:
    branch_name = f"feature/{service}"
    print(f"Creating branch: {branch_name}")

    # Create a new branch
    run_command(["git", "checkout", "-b", branch_name])

    # Push the branch to the remote repository
    run_command(["git", "push", "-u", "origin", branch_name])

print("All branches created and pushed successfully!")
