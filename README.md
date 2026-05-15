# 🚀 Task Management API

A modern and scalable **Task Management REST API** built using **FastAPI** and **PostgreSQL** with secure JWT authentication, modular architecture, and clean backend development practices.

This project demonstrates production-level backend architecture using Python with proper separation of concerns, database migrations, authentication, and CRUD operations.

---

# ✨ Features

- 🔐 JWT Authentication & Authorization
- 👤 User Registration & Login
- 📝 Task CRUD Operations
- 🛡️ Protected Routes
- ⚡ FastAPI High-Performance APIs
- 🧠 Clean & Modular Architecture
- 🗂️ SQLAlchemy ORM Integration
- 🔄 Alembic Database Migrations
- 📦 Pydantic Data Validation
- 🌱 Environment-Based Configuration
- 📚 Interactive Swagger API Docs

---

# 🏗️ Architecture

This project follows:

- 🧱 Clean Architecture
- 📦 Modular Structure
- 🧠 Controller-Based Business Logic
- 🗂️ Repository & DTO Pattern

### 🔄 Architecture Layers

API Routes → Controllers → Database Models

# 🛠️ Tech Stack

| Technology     | Usage                     |
| -------------- | ------------------------- |
| 🐍 Python      | Main Programming Language |
| ⚡ FastAPI      | Backend Framework         |
| 🗄️ PostgreSQL | Relational Database       |
| 🔗 SQLAlchemy  | ORM                       |
| 🔄 Alembic     | Database Migration        |
| 🔐 JWT         | Authentication            |
| 📦 Pydantic    | Data Validation           |
| 🚀 Uvicorn     | ASGI Server               |

---

# 🔐 Authentication

The API uses **JWT (JSON Web Tokens)** for secure authentication and authorization.

### Protected Routes Require:

```http
Authorization: Bearer <token>
```

---

# 📡 API Modules

## 👤 User Module

* Register User
* Login User
* Verify Authentication Token

## 📝 Task Module

* Create Task
* Get All Tasks
* Get Task Details
* Update Task
* Delete Task

---

# 🗃️ Database Schema

## 👤 User Table

| Field         | Type    |
| ------------- | ------- |
| id            | Integer |
| name          | String  |
| username      | String  |
| email         | String  |
| hash_password | String  |

---

## 📝 Task Table

| Field       | Type        |
| ----------- | ----------- |
| id          | Integer     |
| title       | String      |
| description | String      |
| status      | Boolean     |
| user_id     | Foreign Key |

---

# 📚 API Documentation

FastAPI automatically provides interactive API documentation using Swagger UI.

```bash
/docs
```

---

# 🎯 Project Goals

This project was built to showcase:

* Backend Development Skills
* FastAPI Framework Knowledge
* Authentication & Security
* Database Design
* Clean Architecture Principles
* REST API Development
* Production-Level Project Structure
---

```
```
