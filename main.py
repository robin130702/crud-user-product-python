from fastapi import FastAPI
from database import *
from route.user_route import user_router
from route.product_route import product_route

# Create tables in the database
Base.metadata.create_all(bind=engine)
# Initialize FastAPI app
app = FastAPI()
app.include_router(user_router)
app.include_router(product_route)





