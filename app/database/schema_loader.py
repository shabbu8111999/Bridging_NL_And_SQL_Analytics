from sqlalchemy import inspect
from app.database.connection import engine

def load_schema() -> str:
    inspector = inspect(engine)
    schema_desc = []

    tables = sorted(inspector.get_table_names())
    if not tables:
        return ""

    for table in tables:
        cols = inspector.get_columns(table)
        col_defs = [
            f"{col['name']}:{str(col['type'])}"
            for col in cols
        ]
        schema_desc.append(f"{table}({', '.join(col_defs)})")

    return "\n".join(schema_desc)
