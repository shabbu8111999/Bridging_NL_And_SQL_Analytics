from sqlalchemy import inspect
from app.database.connection import engine

def load_schema() -> str:
    inspector = inspect(engine)
    schema_desc = []

    for table in sorted(inspector.get_table_names()):
        cols = inspector.get_columns(table)
        col_names = [
            f"{col['name']}:{col['type']}"
            for col in cols
        ]
        schema_desc.append(f"{table}({', '.join(col_names)})")

    return "\n".join(schema_desc)
