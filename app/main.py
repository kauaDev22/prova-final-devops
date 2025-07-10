from fastapi import FastAPI
from sqlalchemy import create_engine, text

app = FastAPI()

DATABASE_URL = "postgresql://postgres:postgres@postgres-service:5432/postgres"

engine = create_engine(DATABASE_URL)

@app.get("/")
def read_root():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT 'Conectado ao PostgreSQL com sucesso!'"))
        return {"message": result.scalar()}
