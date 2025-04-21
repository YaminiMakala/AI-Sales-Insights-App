from sqlalchemy import create_engine, Column, Integer, String, Float, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

DATABASE_URL = "sqlite:///./sales.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# ================= Sales Model =================
class SalesData(Base):
    __tablename__ = "sales_data"
    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date)
    customer_name = Column(String)
    product_name = Column(String)
    amount = Column(Float)
    status = Column(String)

Base.metadata.create_all(bind=engine)

# ================= Get All Sales =================
def get_all_sales():
    session = SessionLocal()
    sales = session.query(SalesData).all()
    session.close()
    return sales

# ================= Insert CSV Records =================
def insert_sales_csv(file):
    import csv
    from io import StringIO
    session = SessionLocal()
    content = StringIO(file.getvalue().decode("utf-8"))
    reader = csv.DictReader(content)
    count = 0
    for row in reader:
        sale = SalesData(
            date=datetime.datetime.strptime(row['date'], "%Y-%m-%d").date(),
            customer_name=row['customer_name'],
            product_name=row['product_name'],
            amount=float(row['amount']),
            status=row['status']
        )
        session.add(sale)
        count += 1
    session.commit()
    session.close()
    return count
