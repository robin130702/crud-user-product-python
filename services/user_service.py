
from fastapi import FastAPI , HTTPException,Depends
def get_users_fun(db,UserSchema):
    users = db.query(UserSchema).all()
    return users
def add_user(db,body,UserSchema):
    db_user = db.query(UserSchema).filter(UserSchema.username == body.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    new_user = UserSchema(username=body.username, password=body.password, phone_number=body.phone_number)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
def fetch_user_by_id(db,user_id,UserSchema):
    body = db.query(UserSchema).filter(UserSchema.id == user_id).first()
    if body is None:
        raise HTTPException(status_code=404, detail="UserSchema not found")
    return body
def give_user_by_id(db,user_id,body,UserSchema):
    db_user = db.query(UserSchema).filter(UserSchema.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="body not found")
    

    db_user.username = body.username
    db_user.password = body.password
    db_user.phone_number = body.phone_number
    db.commit()
    db.refresh(db_user)
    return db_user
def remove_user_by_id(db,user_id,UserSchema):
     db_user = db.query(UserSchema).filter(UserSchema.id == user_id).first()
     if db_user is None:
        raise HTTPException(status_code=404, detail="UserSchema not found") 
     db.delete(db_user)
     db.commit()
     return {"message": "UserSchema deleted successfully"}
