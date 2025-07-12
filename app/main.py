from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Substitua pelo IP e porta do frontend ou use ["*"] temporariamente
origins = [
    "http://192.168.56.10:30001",  # frontend
    "http://localhost:30001"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # ou ["*"] só para teste
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Conectado ao PostgreSQL com sucesso!"}
