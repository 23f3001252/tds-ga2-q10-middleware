# FastAPI Middleware Stack Assignment

A production-style **FastAPI** service demonstrating three essential middleware patterns:

* ✅ Request Context Propagation
* ✅ Scoped CORS Policy
* ✅ Per-Client Rate Limiting

## Live Demo

**Base URL**

**https://tds-ga2-q10-middleware.onrender.com**

**Swagger UI**

**https://tds-ga2-q10-middleware.onrender.com/docs**

## Features

### Request Context Middleware

* Reuses the incoming `X-Request-ID` header if present.
* Generates a new UUID when the header is missing.
* Returns the request ID in:

  * Response JSON body
  * `X-Request-ID` response header

### CORS Middleware

* Allows requests only from the assigned origin(s).
* Supports browser preflight (`OPTIONS`) requests.
* Does not use wildcard (`*`) origins.

### Rate Limiting Middleware

* Buckets requests by `X-Client-Id`.
* Limit: **9 requests per 10 seconds** for each client.
* Returns **HTTP 429 (Too Many Requests)** when the limit is exceeded.
* Different client IDs have independent rate-limit buckets.

## API Endpoint

### `GET /ping`

Returns:

```json
{
  "email": "YOUR_EMAIL@example.com",
  "request_id": "generated-or-reused-request-id"
}
```

## Project Structure

```text
middleware-api/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── middleware.py
│   ├── ratelimiter.py
│   └── storage.py
│
├── pyproject.toml
├── uv.lock
└── README.md
```

## Tech Stack

* Python 3
* FastAPI
* Uvicorn
* uv (Python package manager)
* Render

## Run Locally

Clone the repository and install dependencies:

```bash
uv sync
```

Start the development server:

```bash
uv run uvicorn app.main:app --reload
```

Open:

* **API:** http://127.0.0.1:8000/ping
* **Swagger UI:** http://127.0.0.1:8000/docs

## Assignment Requirements Covered

* ✔ Request Context Middleware
* ✔ Scoped CORS Configuration
* ✔ Per-Client Rate Limiting
* ✔ FastAPI Middleware Stack
* ✔ Interactive API Documentation (Swagger)
* ✔ Public Deployment on Render

## Deployment

The application is deployed on Render and is publicly accessible for automated evaluation.

**Live URL:** https://tds-ga2-q10-middleware.onrender.com
