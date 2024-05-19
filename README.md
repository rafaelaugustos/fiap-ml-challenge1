# FIAP API 1

This project is a FastAPI-based web service that scrapes viticulture data from the Embrapa website. It provides endpoints to fetch production, processing, commercialization, importation, and exportation data.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Running the Project](#running-the-project)
- [Authentication](#authentication)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)

## Features

- Fetches viticulture data from Embrapa.
- Provides endpoints for different data categories: production, processing, commercialization, importation, and exportation.
- Supports query parameters for filtering data by year and suboption.
- JWT authentication for secure access to the API endpoints.

## Requirements

- Python 3.7+
- FastAPI
- Requests
- BeautifulSoup4
- Uvicorn (for running the FastAPI application)
- PyJWT (for JWT authentication)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/rafaelaugustos/fiap-ml-challenge1.git
   cd fiap-ml-challenge1
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## Running the Project

1. **Start the FastAPI application:**

   ```bash
   uvicorn main:app --reload
   ```

2. The API will be available at `http://127.0.0.1:8000`.

## Authentication

The API uses JSON Web Tokens (JWT) for authentication. To access the endpoints, you need to obtain a JWT by logging in.

### Obtaining a Token

Make a POST request to the `/login` endpoint with the username and password:

- **URL**: `/login`
- **Method**: `POST`
- **Body**:

```
{
  "username": "test",
  "password": "test"
}
```

Example:

```bash
curl -X POST "http://127.0.0.1:8000/login" -H "Content-Type: application/json" -d '{"username":"test","password":"test"}'
```

You will receive a response with an access token:

```
{
  "access_token": "your_jwt_token"
}
```

### Using the Token

To access the protected endpoints, include the JWT in the Authorization header:

`Authorization: Bearer your_jwt_token`

## Usage

Use the API endpoints to fetch viticulture data. You can use tools like `curl`, `Postman`, or a web browser to interact with the API.

## API Endpoints

### Production Data

- **URL:** `/production`
- **Method:** `GET`
- **Query Parameters:**
  - `year` (optional): The year for which to fetch data. Defaults to the current year.
- **Authorization:** Bearer Token

Example:

```bash
curl -X GET "http://127.0.0.1:8000/production?year=2022" -H "Authorization: Bearer your_jwt_token"
```

### Processing Data

- **URL:** `/processing`
- **Method:** `GET`
- **Query Parameters:**
  - `year` (optional): The year for which to fetch data. Defaults to the current year.
  - `suboption` (optional): The suboption for processing data. Defaults to subopt_01.
- **Authorization:** Bearer Token

Example:

```bash
curl -X GET "http://127.0.0.1:8000/processing?year=2022&suboption=subopt_02" -H "Authorization: Bearer your_jwt_token"
```

### Commercialization Data

- **URL:** `/commercialization`
- **Method:** `GET`
- **Query Parameters:**
  - `year` (optional): The year for which to fetch data. Defaults to the current year.
- **Authorization:** Bearer Token

Example:

```bash
curl -X GET "http://127.0.0.1:8000/commercialization?year=2022" -H "Authorization: Bearer your_jwt_token"
```

### Importation Data

- **URL:** `/importation`
- **Method:** `GET`
- **Query Parameters:**
  - `year` (optional): The year for which to fetch data. Defaults to the current year.
  - `suboption` (optional): The suboption for processing data. Defaults to subopt_01.
- **Authorization:** Bearer Token

Example:

```bash
curl -X GET "http://127.0.0.1:8000/importation?year=2022&suboption=subopt_03" -H "Authorization: Bearer your_jwt_token"
```

### Exportation Data

- **URL:** `/exportation`
- **Method:** `GET`
- **Query Parameters:**
  - `year` (optional): The year for which to fetch data. Defaults to the current year.
  - `suboption` (optional): The suboption for processing data. Defaults to subopt_01.
- **Authorization:** Bearer Token

Example:

```bash
curl -X GET "http://127.0.0.1:8000/exportation?year=2022&suboption=subopt_04" -H "Authorization: Bearer your_jwt_token"
```

## Handling Errors

If the JWT token is invalid or missing, you will receive a 401 Unauthorized error:

```
{
    "detail": "Token has expired"
}
```

or

```
{
    "detail": "Signature verification failed"
}
```
