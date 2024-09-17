from fastapi import APIRouter
from fastapi import HTTPException,Depends
from sqlalchemy.orm import Session
from services.user_service import get_users_fun
from services.user_service import add_user
from services.user_service import give_user_by_id
from services.user_service import fetch_user_by_id
from services.user_service import remove_user_by_id
from  schema.user_schema import UserSchema
from database import get_db
from model.usermodel import UserCreate,UserResponse
user_router=APIRouter()
# Create UserSchema (POST)
@user_router.post("/users/", response_model=UserResponse)
def create_user(body: UserCreate, db :Session= Depends(get_db)):
    try:
        return add_user(db,body,UserSchema)
    except Exception as e:
        print(f"internal server error {str(e)}")
        raise HTTPException(status_code=500,detail=f"internal server error {str(e)}")


# Get All Users (GET)
@user_router.get("/users/", response_model=list[UserResponse])
def get_users(db:Session= Depends(get_db)):
    try:
        return get_users_fun(db,UserSchema)
    except Exception as e:
        print(f"internal server error {str(e)}")
        raise HTTPException(status_code=500,detail=f"internal server error {str(e)}")
@user_router.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db:Session = Depends(get_db)):
    try:
        return fetch_user_by_id (db,user_id,UserSchema)
    except Exception as e: 
        print(f"internal server error {str(e)}")
        raise HTTPException(status_code=500,detail=f"internal server error {str(e)}")

# Get Single UserSchema by ID (GET)

    

# Update UserSchema by ID (PUT)
@user_router.put("/users/{user_id}", response_model=UserResponse)
def update_user(user_id: int, body: UserCreate, db:Session = Depends(get_db)):
    try:
        return give_user_by_id(db,user_id,body,UserSchema)
    except Exception as e:
        print(f"internal server error {str(e)}")
        raise HTTPException(status_code=500,detail=f"internal server error {str(e)}")

# Delete UserSchema by ID (DELETE)
@user_router.delete("/users/{user_id}")
def delete_user(user_id: int, db:Session = Depends(get_db)):
    try:
      return remove_user_by_id(db,user_id,UserSchema)
    except Exception as e:
        print(f"internal server error {str(e)}")
        raise HTTPException(status_code=500,detail=f"internal server error {str(e)}")
