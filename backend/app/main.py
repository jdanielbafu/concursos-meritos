from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings

app = FastAPI(
    title="Concursos Méritos API",
    version="0.1.0",
)

# CORS: permite que Next.js (en otro dominio) hable con esta API
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Ruta de prueba — verifica que el servidor está vivo
@app.get("/health")
def health_check():
    return {"status": "ok", "version": "0.1.0"}

# Aquí irás agregando los routers de cada módulo
# from app.modules.usuarios.router import router as usuarios_router
# app.include_router(usuarios_router, prefix="/api/v1/usuarios")