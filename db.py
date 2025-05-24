import os
from sqlmodel import SQLModel, create_engine


DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+psycopg2://user:password@172.18.0.2:5432/cars_db")
engine = create_engine(DATABASE_URL, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)