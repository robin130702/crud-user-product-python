from pydantic import BaseModel
# Pydantic model for request/response validation
class UserCreate(BaseModel):
    username: str
    password: str
    phone_number: str

class UserResponse(BaseModel):
    id: int
    username: str
    password:str
    phone_number: str