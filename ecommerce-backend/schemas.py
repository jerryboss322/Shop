from pydantic import BaseModel, EmailStr
from typing import Optional, List

class UserSignup(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone_number: str
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    phone_number: Optional[str]
    is_admin: bool
    
    class Config:
        from_attributes = True

class ProductCreate(BaseModel):
    name: str
    description: Optional[str] = None
    price: int
    stock_quantity: int = 0
    category_id: Optional[int] = None
    image_url: Optional[str] = None

class ProductUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[int] = None
    stock_quantity: Optional[int] = None
    is_active: Optional[bool] = None

class CartAdd(BaseModel):
    product_id: int
    quantity: int = 1

class OrderCreate(BaseModel):
    shipping_address: str
    coupon_code: Optional[str] = None
