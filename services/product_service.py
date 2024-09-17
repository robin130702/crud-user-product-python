from fastapi import HTTPException,Depends
from  schema.product_schema import Product
def get_product(db):
    product= db.query(Product).all()
    return product
def add_product(db,body):
    db_product = db.query(Product).filter(Product.product_name == body.product_name).first()
    if db_product:
        raise HTTPException(status_code=400, detail="product already registered")
    new_product = Product(product_name=body.product_name, product_prize=body.product_prize)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product
def fetch_product_by_id(db,product_id):
    product = db.query(Product).filter(Product.product_id== product_id).first()
    if product is None:
        raise HTTPException(status_code=404, detail="product not found")
    return product
def update_product_by_id(db,product_id,body):
    db_product= db.query(Product).filter(Product.product_id == product_id).first()
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    db_product.product_name = body.product_name
    db_product.product_prize= body.product_prize
    db.commit()
    db.refresh(db_product)
    return db_product
def remove_product_by_id(db,product_id,Product):
     db_product = db.query(Product).filter(Product.product_id == product_id).first()
     if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found") 
     db.delete(db_product)
     db.commit()
     return {"message": "Product Details deleted successfully"}