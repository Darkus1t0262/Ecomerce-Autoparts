# 🚗 E-Commerce Auto Parts Microservices

This project is a **microservices-based eCommerce platform** for selling **auto parts**. The architecture is **API-driven** with services handling **authentication, products, orders, and a database** using **AWS EC2, MongoDB, and Docker containers**.

---

## 🏗 **Architecture Overview**
### **Microservices**
| Service | Description | Port |
|---------|------------|------|
| 🛂 **Auth Service** | Handles user authentication (JWT-based) | `3000` |
| 🛒 **Product Service** | Manages product catalog and stock levels | `4000` |
| 📦 **Order Service** | Handles order placement and processing | `5000` |
| 🗄 **MongoDB** | Stores product and order data | `27017` |

---

## 🚀 **How to Run Services**
### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/your-repo/ecommerce-autoparts.git
cd ecommerce-autoparts

---

