from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import get_db
import models, schemas
from auth import get_current_admin

router = APIRouter(prefix="/api/v1", tags=["products"])

@router.get("/categories", response_model=List[schemas.CategoryResponse])
def get_categories(db: Session = Depends(get_db)):
    return db.query(models.Category).all()

@router.get("/products", response_model=List[schemas.ProductResponse])
def get_products(skip: int = 0, limit: int = 50, db: Session = Depends(get_db)):
    return db.query(models.Product).offset(skip).limit(limit).all()

@router.post("/products", response_model=schemas.ProductResponse)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db), admin = Depends(get_current_admin)):
    db_product = models.Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product
