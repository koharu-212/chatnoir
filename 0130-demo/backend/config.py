import os

DB_USER = os.getenv("POSTGRES_USER", "your_db_user")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD", "your_db_password")
DB_HOST = os.getenv("POSTGRES_HOST", "db")
DB_PORT = os.getenv("POSTGRES_PORT", "5432")
DB_NAME = os.getenv("POSTGRES_DB", "your_db_name")

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
