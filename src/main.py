# src/main.py
from fastapi import FastAPI

# Inicializamos la aplicación FastAPI
app = FastAPI(
    title="CSR Valera API",
    description="Backend API for the CSR Valera platform following Hexagonal Architecture.",
    version="1.0.0",
)

# Definimos el endpoint de Health Check solicitado en la tarjeta
@app.get("/api/v1/health", tags=["Health"])
async def health_check():
    """
    Health check endpoint to verify the API is running and ready to accept requests.
    """
    return {
        "status": "ok", 
        "message": "CSR API is running"
    }

# Nota: En el futuro, aquí conectaremos los routers de nuestra capa de infraestructura