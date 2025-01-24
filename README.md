# Ecomerce-Autoparts Microservices Architecture

## Overview
Ecomerce-Autoparts is a distributed e-commerce system for managing auto parts sales and vehicle rentals. The project is built using **microservices architecture**, where each service focuses on a specific domain. This ensures scalability, maintainability, and modularity.

The system uses **REST APIs**, **GraphQL**, and event-driven communication (**SNS/SQS**) to enable seamless interaction between services.

---

## Features
- User management, including authentication and profiles.
- Catalog management for auto parts and vehicle rentals.
- Inventory tracking for stock management.
- Promotions and discounts with validation.
- Order management and payment processing.
- Notifications via email and SMS.
- Analytics for business intelligence.

---

## Architecture Diagram

Below is a high-level diagram showing how the microservices interact with each other:

```plaintext
       ┌──────────────┐          ┌──────────────┐
       │  User Service │          │ Auth Service │
       └───────┬───────┘          └──────┬──────┘
               │                          │
    ┌─────────▼─────────┐         ┌──────▼────────┐
    │   Catalog Service  │         │ Promotion Svc │
    └─────────┬──────────┘         └──────┬───────┘
              │                           │
   ┌─────────▼──────────┐      ┌─────────▼──────────┐
   │ Inventory Service   │      │   Cart Service     │
   └─────────┬──────────┘      └─────────┬──────────┘
             │                            │
   ┌─────────▼──────────┐      ┌─────────▼──────────┐
   │   Order Service     │      │ Notification Svc  │
   └─────────┬──────────┘      └─────────┬──────────┘
             │                            │
   ┌─────────▼──────────┐      ┌─────────▼──────────┐
   │  Payment Service    │      │  Analytics Svc     │
   └─────────────────────┘      └────────────────────┘
