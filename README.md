# ShopHub - Complete Ecommerce Platform

Full-stack ecommerce with FastAPI backend, React frontend, and Resend email integration.

## Quick Start

### 1. Backend Setup
```bash
cd ecommerce-backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# IMPORTANT: Add your Resend API key
cp .env.example .env
# Edit .env and replace: RESEND_API_KEY=re_xxxxxxxxx
# Get your key from: https://resend.com/api-keys

python seed.py
python -m uvicorn main:app --reload
```
Backend runs at http://localhost:8000

### 2. Frontend Setup
```bash
cd ecommerce-frontend
npm install
npm run dev
```
Frontend runs at http://localhost:5173

## Resend API Setup

1. Go to https://resend.com
2. Create free account
3. Get API key (starts with re_)
4. Add to ecommerce-backend/.env:
   ```
   RESEND_API_KEY=re_your_actual_key_here
   FROM_EMAIL=onboarding@resend.dev
   ```

## Test Accounts

After running `python seed.py`:

**Admin:**
- Email: admin@lagosstore.ng
- Password: Admin123!

**Customer:**
- Email: customer@test.com
- Password: Password123!

## Features

✅ User signup/login with JWT
✅ Product catalog
✅ Shopping cart
✅ Checkout & orders
✅ Admin dashboard
✅ Email notifications (Resend)
✅ Role-based access

## Project Structure

```
ecommerce-backend/
├── main.py           # FastAPI routes
├── models.py         # Database models
├── schemas.py        # Pydantic schemas
├── auth.py           # JWT authentication
├── email_service.py  # Resend integration ← YOUR API KEY HERE
├── database.py       # DB config
├── config.py         # Settings
└── seed.py           # Test data

ecommerce-frontend/
├── src/
│   ├── components/
│   ├── pages/
│   ├── store/
│   └── api/
```

## API Endpoints

- POST /api/v1/auth/signup
- POST /api/v1/auth/login
- GET /api/v1/products
- POST /api/v1/orders
- GET /api/v1/admin/dashboard (admin only)

## Deployment

Backend: Railway, Render, or Fly.io
Frontend: Vercel or Netlify
Database: Switch to PostgreSQL in production

## Support

API docs: http://localhost:8000/docs
