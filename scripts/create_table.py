from sqlalchemy import text
from app.database.connection import engine

with engine.connect() as conn:
    conn.execute(text("""
        CREATE TABLE IF NOT EXISTS sales (
            id INTEGER PRIMARY KEY,
            product TEXT,
            amount REAL,
            created_at TEXT
        );
    """))
    conn.commit()

print("Tables created successfully")
