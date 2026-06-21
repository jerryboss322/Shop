from database import SessionLocal, engine
from models import Base, User, Category, Product, Coupon
from auth import get_password_hash

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

db = SessionLocal()

# Create admin
admin = User(first_name="Admin", last_name="Store", email="admin@lagosstore.ng", phone_number="+2348000000000", hashed_password=get_password_hash("Admin123!"), is_admin=True, email_verified=True)
db.add(admin)

# Create customer
customer = User(first_name="Test", last_name="Customer", email="customer@test.com", phone_number="+2348012345678", hashed_password=get_password_hash("Password123!"), is_admin=False, email_verified=True)
db.add(customer)

# Categories
cats = [
    Category(name="Fashion", slug="fashion", description="Clothing and accessories"),
    Category(name="Electronics", slug="electronics", description="Gadgets and devices"),
    Category(name="Phones", slug="phones", description="Mobile phones"),
    Category(name="Home", slug="home", description="Home essentials"),
]
for c in cats:
    db.add(c)
db.commit()

# Products
products = [
    Product(name="Ankara Dress", description="Beautiful Ankara print", price=28500, stock_quantity=12, category_id=1, image_url="https://images.unsplash.com/photo-1594633312681-425c7b97ccd1?w=800"),
    Product(name="Nike Air Max", description="Comfortable sneakers", price=65000, stock_quantity=8, category_id=1, image_url="https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=800"),
    Product(name="iPhone 15 Pro", description="Latest iPhone", price=850000, stock_quantity=5, category_id=3, image_url="https://images.unsplash.com/photo-1592750475338-74b7b21085ab?w=800"),
    Product(name="Sony Headphones", description="Noise cancelling", price=125000, stock_quantity=15, category_id=2, image_url="https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=800"),
]
for p in products:
    db.add(p)

# Coupons
coupons = [
    Coupon(code="WELCOME10", discount_percent=10, max_uses=100),
    Coupon(code="SAVE15", discount_percent=15, max_uses=50),
]
for c in coupons:
    db.add(c)

db.commit()
print("✓ Database seeded!")
print("Admin: admin@lagosstore.ng / Admin123!")
print("Customer: customer@test.com / Password123!")
