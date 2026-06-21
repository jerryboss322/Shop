from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from datetime import datetime
import uvicorn

from database import engine, get_db
from models import Base, User, Product, Category, Cart, CartItem, Order, OrderItem, Coupon
from schemas import *
from auth import get_password_hash, verify_password, create_access_token, get_current_user, get_current_admin
from email_service import send_welcome_email, send_order_confirmation
from config import settings

Base.metadata.create_all(bind=engine)
app = FastAPI(title="ShopHub API", version="1.0.0")

app.add_middleware(CORSMiddleware, allow_origins=settings.ALLOWED_ORIGINS, allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

@app.post("/api/v1/auth/signup")
def signup(user: UserSignup, db: Session = Depends(get_db)):
    if db.query(User).filter(User.email == user.email).first():
        raise HTTPException(400, "Email exists")
    db_user = User(first_name=user.first_name, last_name=user.last_name, email=user.email, phone_number=user.phone_number, hashed_password=get_password_hash(user.password), is_admin=False, email_verified=True)
    db.add(db_user); db.commit(); db.refresh(db_user)
    try: send_welcome_email(user.email, user.first_name)
    except: pass
    return db_user

@app.post("/api/v1/auth/login")
def login(creds: UserLogin, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == creds.email).first()
    if not user or not verify_password(creds.password, user.hashed_password):
        raise HTTPException(401, "Invalid")
    token = create_access_token({"sub": user.email, "admin": user.is_admin})
    return {"access_token": token, "token_type": "bearer", "user": user.to_dict()}

@app.get("/api/v1/products")
def list_products(skip: int = 0, limit: 20 = 20, db: Session = Depends(get_db)):
    return [p.to_dict() for p in db.query(Product).filter(Product.is_active == True).offset(skip).limit(limit).all()]

@app.post("/api/v1/orders")
def create_order(order_data: OrderCreate, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    cart = db.query(Cart).filter(Cart.user_id == current_user.id).first()
    if not cart or not cart.items: raise HTTPException(400, "Empty cart")
    subtotal = sum(i.product.price * i.quantity for i in cart.items)
    total = subtotal + 2500 + int(subtotal * 0.075)
    order = Order(user_id=current_user.id, order_number=f"ORD-{datetime.now().strftime('%Y%m%d')}-{current_user.id}", subtotal=subtotal, shipping=2500, tax=int(subtotal*0.075), total=total, shipping_address=order_data.shipping_address, status="pending")
    db.add(order); db.commit()
    for ci in cart.items:
        db.add(OrderItem(order_id=order.id, product_id=ci.product_id, quantity=ci.quantity, price=ci.product.price))
    db.query(CartItem).filter(CartItem.cart_id == cart.id).delete(); db.commit()
    try:
        items = [{"name": i.product.name, "qty": i.quantity, "price": i.product.price} for i in cart.items]
        send_order_confirmation(current_user.email, order.order_number, items, total, current_user.first_name)
    except: pass
    return order.to_dict()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
