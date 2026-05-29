import os 
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from core.config import DATABASE_URL
# 2. Add a safety check so it tells you exactly what's wrong if it fails again
if not DATABASE_URL:
    raise ValueError("DATABASE_URL is missing! Check that it is saved inside your .quant_env file.")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()