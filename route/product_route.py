from fastapi import APIRouter
from fastapi import HTTPException,Depends,Query
from database import get_db 
from model.productmodel import ProductCreate,ProductResponse
from sqlalchemy.orm import Session
from services.product_service import add_product
from services.product_service import get_product
from services.product_service import fetch_product_by_id
from services.product_service import update_product_by_id
from services.product_service import remove_product_by_id
from database import get_db
from schema.product_schema import Product


product_route=APIRouter()
# Create UserSchema (POST)
@product_route.post("/product/",response_model=ProductResponse)
def product_user(body: ProductCreate, db :Session= Depends(get_db)):
    try:
        return add_product(db,body)
    except Exception as e:
        print(f"internal server error {str(e)}")
        raise HTTPException(status_code=500,detail=f"internal server error {str(e)}")
@product_route.get("/product/", response_model=list[ProductResponse])
def get_product_detail(db:Session= Depends(get_db)):
    try:
        return get_product(db)
    except Exception as e:
        print(f"internal server error {str(e)}")
        raise HTTPException(status_code=500,detail=f"internal server error {str(e)}")
@product_route.get("/product/{product_id}",response_model=ProductResponse)
def get_user(product_id: int, db:Session = Depends(get_db),
    email:str=Query(...),
    age:int=Query(...)
):
    try:
        return fetch_product_by_id (db,product_id)
    except Exception as e:
        print(f"internal server error {str(e)}")
        raise HTTPException(status_code=500,detail=f"internal server error {str(e)}")
@product_route.put("/product/{product_id}", response_model=ProductResponse)
def update_product(product_id: int, body: ProductCreate, db:Session = Depends(get_db)):
    try:
        return update_product_by_id(db,product_id,body)
    except Exception as e:
        print(f"internal server error {str(e)}")
        raise HTTPException(status_code=500,detail=f"internal server error {str(e)}")
@product_route.delete("/product/{product_id}")
def delete_product(product_id: int, db:Session = Depends(get_db)):
    try:
      return remove_product_by_id(db,product_id,Product)
    except Exception as e:
        print(f"internal server error {str(e)}")
        raise HTTPException(status_code=500,detail=f"internal server error {str(e)}")