from app.database.schema_loader import load_schema

def get_schema_context():
    return load_schema()
