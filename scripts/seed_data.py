from sqlalchemy import text
from app.database.connection import engine

def seed_sales_data():
    with engine.connect() as conn:
        conn.execute(text("""
            INSERT INTO sales (product, amount, created_at)
            VALUES
            ('Laptop', 80000, '2024-01-10'),
            ('Phone', 40000, '2024-02-15'),
            ('Tablet', 30000, '2024-03-20');
        """))
        conn.commit()

    print("Sample sales data inserted successfully")

if __name__ == "__main__":
    seed_sales_data()
