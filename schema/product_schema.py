from pydantic import BaseModel
from database import Base
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
class Product(Base):
    __tablename__ = "products_table"
    product_id=Column(Integer, primary_key=True, index=True)
    product_name= Column(String, unique=True, index=True, nullable=False)
    product_prize=Column(String, nullable=False)
