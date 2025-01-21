import os

# Lista de 20 microservicios con sus lenguajes
services = {
    "user-service": "python",
    "authentication-service": "python",
    "catalog-service": "go",
    "inventory-service": "python",
    "search-service": "python",
    "cart-service": "csharp",
    "order-service": "python",
    "shipping-service": "nodejs",
    "payment-service": "go",
    "billing-service": "go",
    "rental-service": "csharp",
    "vehicle-management-service": "csharp",
    "notification-service": "nodejs",
    "email-service": "nodejs",
    "sms-service": "nodejs",
    "recommendation-service": "go",
    "analytics-service": "go",
    "audit-log-service": "python",
    "promotions-service": "nodejs",
    "customer-support-service": "csharp"
}

# Archivos iniciales por lenguaje
def create_initial_files(service_path, language):
    if language == "python":
        # Archivos para servicios en Python
        with open(os.path.join(service_path, "src", "app.py"), "w") as f:
            f.write(python_app_template())
        with open(os.path.join(service_path, "requirements.txt"), "w") as f:
            f.write("Flask\n")

    elif language == "go":
        # Archivos para servicios en Go
        with open(os.path.join(service_path, "src", "main.go"), "w") as f:
            f.write(go_app_template())

    elif language == "csharp":
        # Archivos para servicios en C# (.NET Core)
        os.makedirs(os.path.join(service_path, "src"), exist_ok=True)
        with open(os.path.join(service_path, "src", "Program.cs"), "w") as f:
            f.write(csharp_app_template())
        with open(os.path.join(service_path, "src", f"{service_path.split(os.sep)[-1].capitalize()}.csproj"), "w") as f:
            f.write(csharp_project_template())

    elif language == "nodejs":
        # Archivos para servicios en Node.js
        with open(os.path.join(service_path, "src", "app.js"), "w") as f:
            f.write(nodejs_app_template())
        with open(os.path.join(service_path, "package.json"), "w") as f:
            f.write(nodejs_package_template())


# Plantillas para los lenguajes
def python_app_template():
    return """from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Python Microservice!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
"""

def go_app_template():
    return """package main

import (
    "fmt"
    "net/http"
)

func handler(w http.ResponseWriter, r *http.Request) {
    fmt.Fprintf(w, "Hello from Go Microservice!")
}

func main() {
    http.HandleFunc("/", handler)
    http.ListenAndServe(":8080", nil)
}
"""

def csharp_app_template():
    return """using Microsoft.AspNetCore.Builder;
using Microsoft.Extensions.Hosting;

var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

app.MapGet("/", () => "Hello from C# Microservice!");

app.Run();
"""

def csharp_project_template():
    return """<Project Sdk="Microsoft.NET.Sdk.Web">

  <PropertyGroup>
    <TargetFramework>net6.0</TargetFramework>
  </PropertyGroup>

</Project>
"""

def nodejs_app_template():
    return """const express = require("express");
const app = express();

app.get("/", (req, res) => {
    res.send("Hello from Node.js Microservice!");
});

app.listen(3000, () => {
    console.log("Node.js microservice running on port 3000");
});
"""

def nodejs_package_template():
    return """{
  "name": "notification-service",
  "version": "1.0.0",
  "main": "src/app.js",
  "scripts": {
    "start": "node src/app.js"
  },
  "dependencies": {
    "express": "^4.18.2"
  }
}
"""

# Crear la estructura del proyecto
def create_service_structure(root_dir):
    for service, language in services.items():
        service_path = os.path.join(root_dir, "services", service)

        # Crear carpetas principales
        os.makedirs(os.path.join(service_path, "src"), exist_ok=True)

        # Crear archivos iniciales
        create_initial_files(service_path, language)
        print(f"✅ {service} creado con {language}")

# Ejecutar el script
if __name__ == "__main__":
    root_directory = os.getcwd()  # FIX: Use current working directory directly
    create_service_structure(root_directory)
    print("🚀 ¡Estructura del proyecto creada exitosamente!")
