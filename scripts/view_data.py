from sqlalchemy import text
from app.database.connection import engine

with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM sales"))
    rows = result.fetchall()

    for row in rows:
        print(row)
