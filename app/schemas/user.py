from pydantic import EmailStr, BaseModel, Field


class UserBase(BaseModel):
    email: EmailStr = Field(default="", min_length=3, max_length=50)


class UserCreate(UserBase):
    password: str = Field(default="", min_length=3, max_length=50)


class User(UserBase):
    id: int
    is_active: bool = True

    class Config:
        from_attributes = True
