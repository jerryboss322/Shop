from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import os

from database import engine, Base
import models
from auth import router as auth_router
from products import router as products_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield
    print("Shutting down...")

app = FastAPI(
    title="ShopHub API",
    version="1.0.0",
    lifespan=lifespan
)

origins = os.getenv("ALLOWED_ORIGINS", "http://localhost:3000,https://shop-blush-nine.vercel.app").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(products_router)

@app.get("/")
def root():
    return {"message": "ShopHub API is running", "status": "ok"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}
