# 🚀 Crypto API - Django REST Framework

A Django-based REST API for managing **crypto prices** and **organizations**, built with **Django REST Framework (DRF)**, **Celery**, and **Redis**.

## 📌 Features
- ✅ **CRUD APIs** for organizations & crypto prices
- ✅ **JWT Authentication**
- ✅ **Filtering, Pagination, and Ordering**
- ✅ **Celery & Redis for background tasks**
- ✅ **Dockerized Deployment**
- ✅ **Automated Crypto Price Updates** (via CoinGecko API)

---

## 🛠 **Tech Stack**
- **Backend:** Django, Django REST Framework
- **Database:** SQLite / Redis
- **Caching & Task Queue:** Redis + Celery
- **Authentication:** JWT (Django Simple JWT)

## **Features to do**
- **Deployment:** Docker, Render, AWS

---

## 🔧 **Installation & Setup**

### 1. **Clone the Repository**
```sh
git clone https://github.com/yourusername/crypto-api.git
cd crypto-api

```
### 2. **Create Virtual Environment**
```sh
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate      # Windows

```

### 3. **Install the dependecies**
```sh
pip install -r requirements.txt
```

### 4. **Run Migrations**
```sh
python manage.py migrate
```

### 5. **Create Superuser**
```sh
python manage.py createsuperuser
```

### 6. **Run Development Server**
```sh
python manage.py runserver
```
📌 API will be available at: http://127.0.0.1:8000/api/

## 🔑 **Authentication**

This API uses JWT authentication.
**Generate Token**
```sh
POST /api/token/
{
    "username": "yourusername",
    "password": "yourpassword"
}

```
**Use Token in Requests**
```http
Authorization: Bearer <your_access_token>
```

## 📡 **API Endpoints**

| Method  | Endpoint                      | Description                         | Auth Required |
|---------|--------------------------------|-------------------------------------|--------------|
| **POST** | `/api/token/`                 | Get JWT token                      | ❌ No        |
| **POST** | `/api/token/refresh/`         | Refresh JWT token                  | ✅ Yes       |
| **GET**  | `/api/organizations/`         | List all organizations             | ✅ Yes       |
| **POST** | `/api/organizations/`         | Create a new organization          | ✅ Yes       |
| **GET**  | `/api/organizations/{id}/`    | Get organization details           | ✅ Yes       |
| **PUT**  | `/api/organizations/{id}/`    | Update organization (owner only)   | ✅ Yes       |
| **DELETE** | `/api/organizations/{id}/`  | Delete organization (owner only)   | ✅ Yes       |
| **GET**  | `/api/crypto-prices/`         | List all crypto prices             | ✅ Yes       |
| **POST** | `/api/crypto-prices/`         | Add new crypto price               | ✅ Yes       |
| **GET**  | `/api/crypto-prices/{id}/`    | Get crypto price details           | ✅ Yes       |
| **PUT**  | `/api/crypto-prices/{id}/`    | Update crypto price                | ✅ Yes       |
| **DELETE** | `/api/crypto-prices/{id}/`  | Delete crypto price                | ✅ Yes       |

##⏳ **Automated Crypto Price Updates**

This project fetches crypto prices from CoinGecko API every 5 minutes using Celery and Redis.
### Start Celery Worker
```sh
celery -A crypto_org worker --loglevel=info
```
### Start Celery Beat (Scheduler)
```sh
celery -A crypto_org beat --loglevel=info
```
## 🔗 **Contributing**

Feel free to fork this repo and submit pull requests!

##📜 **License**

This project is licensed under the MIT License.


---

### ✅ **What This README Covers**
✔ **Project Overview**  
✔ **Installation & Setup**  
✔ **Authentication Instructions**  
✔ **API Endpoints**  
✔ **Automated Crypto Price Updates**  


---
