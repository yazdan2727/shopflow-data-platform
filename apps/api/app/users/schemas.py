from pydantic import BaseModel, EmailStr, ConfigDict


class UserCreate(BaseModel):
    full_name: str
    email: EmailStr


class UserResponse(BaseModel):
    id: str
    full_name: str
    email: EmailStr

    model_config = ConfigDict(from_attributes=True)