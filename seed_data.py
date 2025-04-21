from db import SalesData, SessionLocal
import datetime

def seed():
    session = SessionLocal()
    data = [
        SalesData(date=datetime.date(2024, 4, 1), customer_name="Alice", product_name="AI Report", amount=120.5, status="Completed"),
        SalesData(date=datetime.date(2024, 4, 2), customer_name="Bob", product_name="LLM API", amount=200.0, status="Pending"),
        SalesData(date=datetime.date(2024, 4, 3), customer_name="Carol", product_name="Training", amount=340.0, status="Completed"),
    ]
    session.add_all(data)
    session.commit()
    session.close()
    print("Sample data inserted!")

if __name__ == "__main__":
    seed()
