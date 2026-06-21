import resend
import os
from typing import Optional
from config import settings

# Initialize Resend - REPLACE re_xxxxxxxxx WITH YOUR REAL KEY
resend.api_key = settings.RESEND_API_KEY

FROM_EMAIL = settings.FROM_EMAIL or "onboarding@resend.dev"

def send_email(to: str, subject: str, html: str, text: Optional[str] = None) -> dict:
    """Base email sender using Resend"""
    try:
        params = {
            "from": f"Lagos Store <{FROM_EMAIL}>",
            "to": [to],
            "subject": subject,
            "html": html,
        }
        if text:
            params["text"] = text
        email = resend.Emails.send(params)
        return {"success": True, "id": email.get("id")}
    except Exception as e:
        print(f"Email error: {e}")
        return {"success": False, "error": str(e)}

def send_welcome_email(to: str, first_name: str):
    html = f"""
    <!DOCTYPE html><html><head><meta charset="utf-8"><style>
      body{{font-family:-apple-system,sans-serif;margin:0;padding:0;background:#f5f5f5}}
      .container{{max-width:600px;margin:40px auto;background:white;border-radius:12px;overflow:hidden}}
      .header{{background:#008751;padding:32px;text-align:center}}
      .header h1{{color:white;margin:0;font-size:28px}}
      .content{{padding:32px}}
      .button{{display:inline-block;background:#008751;color:white;padding:14px 28px;text-decoration:none;border-radius:8px;font-weight:600;margin:20px 0}}
    </style></head><body>
      <div class="container">
        <div class="header"><h1>Welcome to Lagos Store</h1></div>
        <div class="content">
          <h2>Hi {first_name},</h2>
          <p>Thanks for joining Nigeria's best marketplace!</p>
          <a href="#" class="button">Start Shopping</a>
        </div>
      </div>
    </body></html>
    """
    return send_email(to, "Welcome to Lagos Store 🛍️", html)

def send_order_confirmation(to: str, order_id: str, items: list, total: int, first_name: str):
    items_html = "".join([f"<tr><td style='padding:12px 0;border-bottom:1px solid #eee'>{i['name']} × {i['qty']}</td><td style='text-align:right'>{i['price']*i['qty']:,}</td></tr>" for i in items])
    html = f"""
    <!DOCTYPE html><html><body style="font-family:sans-serif;background:#f5f5f5;margin:0;padding:40px">
      <div style="max-width:600px;margin:0 auto;background:white;border-radius:12px;overflow:hidden">
        <div style="background:#008751;padding:24px;color:white"><h2>Order Confirmed #{order_id}</h2></div>
        <div style="padding:32px">
          <p>Hi {first_name},</p>
          <table style="width:100%;margin:24px 0">{items_html}</table>
          <p style="text-align:right;font-size:20px;font-weight:700">Total: ₦{total:,}</p>
        </div>
      </div>
    </body></html>
    """
    return send_email(to, f"Order Confirmed #{order_id}", html)

def send_password_reset(to: str, reset_link: str, first_name: str):
    html = f"""<div style="font-family:sans-serif;max-width:600px;margin:40px auto;background:white;padding:32px;border-radius:12px">
      <h2>Reset Password</h2><p>Hi {first_name},</p>
      <a href="{reset_link}" style="display:inline-block;background:#008751;color:white;padding:14px 28px;text-decoration:none;border-radius:8px">Reset Password</a>
    </div>"""
    return send_email(to, "Reset your password", html)
