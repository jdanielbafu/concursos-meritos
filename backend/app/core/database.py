from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

# Motor de conexión a PostgreSQL
engine = create_engine(settings.DATABASE_URL)

# Fábrica de sesiones (cada request usa su propia sesión)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Clase base de la que heredarán todos los modelos
Base = declarative_base()

# Dependencia de FastAPI — proporciona una sesión y la cierra al terminar
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()