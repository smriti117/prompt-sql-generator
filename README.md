# Prompt SQL Generator Application

A FastAPI-based application for generating and executing SQL queries via WebSockets.

## Prerequisites

- Python 3.10+
- Docker and Docker Compose
- PostgreSQL (via Docker)

## Setup and Running

Follow these steps to get the application up and running:

### 1. Clone the Repository

```bash
git clone <repository_url>
cd ai-analytics
```

### 2. Create and Activate Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Setup Environment Variables

Create a `.env` file from the example:

```bash
cp .env.example .env
```

Ensure you update the `.env` file with your database credentials and LLM provider details.

### 5. Start the Database

Run the PostgreSQL container in the background:

```bash
docker compose up -d
```

### 6. Check Migration Status

Verify the current state of database migrations:

```bash
alembic current
```

### 7. Run Migrations

Apply all pending migrations to the database:

```bash
alembic upgrade head
```

### 8. Seed Initial Data

Populate the database with sample user data:

```bash
python -m app.db.seed
```

### 9. Start the Application

Run the FastAPI server with auto-reload enabled:

```bash
uvicorn main:app --reload
```

## Testing the WebSocket

Once the application is running, you can test the query generation and execution flow using the provided test client:

```bash
# In a separate terminal
python ws_test_client.py
```

The test client will connect to `ws://localhost:8000/ws/query` and send a sample prompt (e.g., "show all users"). You will see the stages of processing:

1. `generating_sql`
2. `generated_sql` (shows the SQL statement)
3. `executing`
4. `done` (shows the results)
