from sqlalchemy import text
from app.database.connection import engine

ALLOWED_KEYWORDS = {"select"}

def execute_query(sql: str):
    sql_clean = sql.strip().lower()

    if not any(sql_clean.startswith(k) for k in ALLOWED_KEYWORDS):
        raise ValueError("Only SELECT queries are allowed")

    with engine.connect() as conn:
        result = conn.execute(text(sql))
        rows = result.fetchall()
        columns = result.keys()
        
        return [dict(zip(columns, row)) for row in rows]
