from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    phone_number = Column(String(20))
    hashed_password = Column(String(255), nullable=False)
    is_admin = Column(Boolean, default=False)
    email_verified = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    orders = relationship("Order", back_populates="user")
    cart = relationship("Cart", back_populates="user", uselist=False)
    
    def to_dict(self):
        return {"id": self.id, "first_name": self.first_name, "last_name": self.last_name, "email": self.email, "phone_number": self.phone_number, "is_admin": self.is_admin, "created_at": self.created_at.isoformat() if self.created_at else None}

class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)
    slug = Column(String(100), unique=True)
    description = Column(Text)
    products = relationship("Product", back_populates="category")
    
    def to_dict(self):
        return {"id": self.id, "name": self.name, "slug": self.slug, "description": self.description}

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), nullable=False)
    description = Column(Text)
    price = Column(Integer, nullable=False)
    stock_quantity = Column(Integer, default=0)
    category_id = Column(Integer, ForeignKey("categories.id"))
    image_url = Column(String(500))
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    category = relationship("Category", back_populates="products")
    
    def to_dict(self):
        return {"id": self.id, "name": self.name, "description": self.description, "price": self.price, "stock_quantity": self.stock_quantity, "category_id": self.category_id, "image_url": self.image_url, "is_active": self.is_active, "category": self.category.to_dict() if self.category else None}

class Cart(Base):
    __tablename__ = "carts"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    user = relationship("User", back_populates="cart")
    items = relationship("CartItem", back_populates="cart", cascade="all, delete-orphan")
    
    def to_dict(self):
        return {"id": self.id, "user_id": self.user_id, "items": [item.to_dict() for item in self.items], "total": sum(item.product.price * item.quantity for item in self.items)}

class CartItem(Base):
    __tablename__ = "cart_items"
    id = Column(Integer, primary_key=True, index=True)
    cart_id = Column(Integer, ForeignKey("carts.id"))
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(Integer, default=1)
    cart = relationship("Cart", back_populates="items")
    product = relationship("Product")
    
    def to_dict(self):
        return {"id": self.id, "product_id": self.product_id, "quantity": self.quantity, "product": self.product.to_dict() if self.product else None}

class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    order_number = Column(String(50), unique=True, index=True)
    subtotal = Column(Integer, nullable=False)
    shipping = Column(Integer, default=0)
    tax = Column(Integer, default=0)
    discount = Column(Integer, default=0)
    total = Column(Integer, nullable=False)
    status = Column(String(20), default="pending")
    shipping_address = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    user = relationship("User", back_populates="orders")
    items = relationship("OrderItem", back_populates="order", cascade="all, delete-orphan")
    
    def to_dict(self):
        return {"id": self.id, "order_number": self.order_number, "subtotal": self.subtotal, "shipping": self.shipping, "tax": self.tax, "discount": self.discount, "total": self.total, "status": self.status, "shipping_address": self.shipping_address, "created_at": self.created_at.isoformat() if self.created_at else None, "items": [item.to_dict() for item in self.items]}

class OrderItem(Base):
    __tablename__ = "order_items"
    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(Integer, nullable=False)
    price = Column(Integer, nullable=False)
    order = relationship("Order", back_populates="items")
    product = relationship("Product")
    
    def to_dict(self):
        return {"id": self.id, "product_id": self.product_id, "quantity": self.quantity, "price": self.price, "product": self.product.to_dict() if self.product else None}

class Coupon(Base):
    __tablename__ = "coupons"
    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(50), unique=True, index=True, nullable=False)
    discount_percent = Column(Integer, nullable=False)
    max_uses = Column(Integer, default=100)
    uses_count = Column(Integer, default=0)
    is_active = Column(Boolean, default=True)
    expires_at = Column(DateTime(timezone=True))
    
    def to_dict(self):
        return {"id": self.id, "code": self.code, "discount_percent": self.discount_percent, "max_uses": self.max_uses, "uses_count": self.uses_count, "is_active": self.is_active}
