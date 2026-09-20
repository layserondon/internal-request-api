# Internal Request API

REST API developed in Python to manage internal service requests.

The project was created as a practical backend exercise, focusing on API development, route organization, HTTP methods, data handling, and good development practices. It is also part of my ongoing preparation for a career in backend development and AI engineering.

## 🚀 Project Overview

The **Internal Request API** simulates an internal request management system where users can create and consult service requests.

The current version focuses on establishing the API structure and implementing the initial endpoints. Future iterations will introduce persistence, validation, testing, authentication, and additional backend features.

## 🛠️ Technologies

* **Python**
* **Flask**
* **REST API**
* **Git & GitHub**

### Planned technologies

* SQL database
* Automated tests
* API documentation
* Authentication and authorization
* AWS deployment

## 📌 Current Features

* API initialization and configuration
* Organized route structure
* `GET` endpoint for retrieving requests
* `POST` endpoint for creating requests
* JSON request/response handling
* Basic project configuration

## 📂 Project Structure

```text
internal-request-api/
│
├── app/
│   ├── __init__.py
│   ├── routes/
│   │   └── ...
│   │
│   └── ...
│
├── .gitignore
├── requirements.txt
├── README.md
└── ...
```

> The structure will evolve as new layers and features are implemented.

## ⚙️ Running Locally

### 1. Clone the repository

```bash
git clone git@github.com:layserondon/internal-request-api.git
cd internal-request-api
```

### 2. Create a virtual environment

Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the API

```bash
python run.py
```

The API will be available locally according to the application's configured host and port.

## 🔌 API Endpoints

### GET

Retrieves the available internal requests.

```http
GET /requests
```

### POST

Creates a new internal request.

```http
POST /requests
```

Example request:

```json
{
  "title": "Request example",
  "description": "Description of the internal request"
}
```

> Endpoint paths and request fields may change as the project evolves.

## 🧪 Testing

Automated tests are planned for the next development stages.

The testing strategy will cover:

* API endpoints
* HTTP status codes
* Request validation
* Expected responses
* Error handling

## 🗺️ Roadmap

* [x] Initialize API
* [x] Configure routes
* [x] Implement GET endpoint
* [x] Implement POST endpoint
* [ ] Improve project architecture
* [ ] Add request validation
* [ ] Add error handling
* [ ] Add automated tests
* [ ] Add SQL database
* [ ] Implement CRUD operations
* [ ] Add authentication
* [ ] Document API with Swagger/OpenAPI
* [ ] Containerize with Docker
* [ ] Deploy to AWS

## 🎯 Purpose

This project is part of my hands-on learning path in backend development with Python.

The goal is not only to build a functional API, but to progressively apply concepts commonly used in professional software development:

* REST architecture
* Clean code
* Version control
* Database integration
* Automated testing
* API documentation
* Cloud deployment

The project will continue to evolve as these concepts are studied and implemented.

## 👩‍💻 About

Developed by **Layse Rondon**, ADS student at Uninter, currently focusing on Python, backend development, automation, and AI engineering.

GitHub: **@layserondon**
