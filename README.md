# Task Management API with Automated Testing

## Overview
A simple REST API built using FastAPI to create and retrieve tasks. Automated tests validate API responses, required fields, input types, and error handling.

## Technologies
- Python
- FastAPI
- Pydantic
- pytest
- FastAPI TestClient
- HTTPX
- Uvicorn

## Features
- Create a task
- Retrieve all tasks
- Retrieve a task by ID
- Validate required fields
- Reject empty task titles
- Handle requests for nonexistent tasks

## Run Locally

### 1. Create and activate a virtual environment

```powershell
python -m venv venv
venv\Scripts\activate
```

### 2. Install dependencies

```powershell
python -m pip install -r requirements.txt
```

### 3. Start the API

```powershell
python -m uvicorn main:app --reload
```

Open http://127.0.0.1:8000/docs to explore the API.

### 4. Run automated tests

Open a separate terminal in the project directory and run:

```powershell
python -m pytest -v
```

## Testing
The test suite checks successful task creation, missing required fields, empty titles, invalid input types, task-list responses, retrieval of existing tasks, and handling of nonexistent task IDs.

## Limitations
Tasks are stored in memory and are not persisted when the application restarts. This project is intended as a learning exercise in API development and automated testing.