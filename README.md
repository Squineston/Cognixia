# 🏦 Simple Bank Application

A full-stack banking system built to demonstrate **MVC Architecture**, **RESTful APIs**, **Database Integration**, and **Frontend-Backend Integration**.

---

## 📌 Project Overview

This application allows users to:
* Create a bank account
* Fetch account details & current balance
* Deposit funds
* Withdraw funds (with business rule validation)
* View complete transaction history

---

## 🛠️ Tech Stack & Tools

* **Backend Framework:** Python (FastAPI)
* **Database:** MySQL / SQLite & SQLAlchemy ORM
* **Frontend:** React (Vite) / HTML5, CSS3, JavaScript
* **Documentation & Testing:** Swagger UI, Postman[cite: 1]
* **Version Control:** Git & GitHub[cite: 1]

---

## 🌿 Git Branch Progression

This repository is structured across multiple branches to demonstrate iterative development:

1. **`Console App`** – CLI version in terminal using basic data structures.
2. **`API no DB`** – FastAPI REST API running with in-memory storage.
3. **`API DB`** – Full MVC REST API integrated with SQLAlchemy & Database[cite: 1].
4. **`React`** – Full-Stack application integrated with a React UI[cite: 1].

---

## 📐 High-Level Architecture

```text
Frontend (React / HTML) 
       │
       ▼
REST API (Controller Layer)
       │
       ▼
Service Layer (Business Logic & Rules)
       │
       ▼
Repository Layer (Data Access)
       │
       ▼
Database (MySQL / SQLite)
