# 🚗 E-Commerce Auto Parts Microservices
Welcome to the E-Commerce Auto Parts Microservices project! This platform is a microservices-based eCommerce solution designed for selling auto parts. It is built with a robust API-driven architecture, using various services for authentication, product management, order processing, and integration with a MongoDB database, all running inside Docker containers on AWS EC2.

---

# 🏗 Architecture Overview
Microservices Breakdown
This project is composed of multiple microservices, each responsible for a specific domain of the eCommerce platform:

Service	Description	Port
🛂 Auth Service	Handles user authentication using JWT tokens for secure login	                3000
🛒 Product Service	Manages the product catalog, including stock levels and product details  	4000
📦 Order Service	Manages order placements, tracking, and processing	                        5000
🗄 MongoDB	Stores product and order data, providing a scalable database solution	             27017
---

## 🚀 **How to Run Services**
### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/your-repo/ecommerce-autoparts.git
cd ecommerce-autoparts

---

