from fastapi import FastAPI
import redis
import os
import psycopg2

app = FastAPI()

@app.get("/api/health")
def health_check():
    # Validar Redis
    r = redis.Redis.from_url(os.getenv("REDIS_URL", "redis://redis:6379/0"))
    r.incr("hits")
    visits = r.get("hits").decode("utf-8")

    # Validar Postgres
    db_status = "Disconnected"
    try:
        conn = psycopg2.connect(os.getenv("DATABASE_URL"))
        conn.close()
        db_status = "Connected"
    except Exception as e:
        db_status = str(e)

    return {
        "status": "online",
        "database": db_status,
        "redis_visits": visits
    }