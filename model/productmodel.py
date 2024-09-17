from pydantic import BaseModel
# Pydantic model for request/response validation
class ProductCreate(BaseModel):
    product_name:str
    product_prize:int
class ProductResponse(BaseModel):
    product_id:int
    product_name:str
    product_prize:int