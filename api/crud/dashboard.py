from sqlalchemy.orm import Session
from api.database.models.order import Order
from datetime import datetime, timedelta
from sqlalchemy import func

def get_latest_orders(db: Session):
    return db.query(Order).order_by(Order.created_at.desc()).limit(1).all()

def get_last_month_revenue(db: Session):
    last_month = datetime.utcnow().replace(day=1) - timedelta(days=1)
    return db.query(func.sum(Order.total)).filter(Order.created_at >= last_month).scalar() or 0

def get_orders_delivered_on_20_feb(db: Session):
    return db.query(Order).filter(Order.status == "delivered", func.date(Order.created_at) == "2025-02-20").all()

def get_last_3_months_revenue(db: Session):
    three_months_ago = datetime.utcnow() - timedelta(days=90)
    return db.query(func.sum(Order.total)).filter(Order.created_at >= three_months_ago).scalar() or 0

def get_pending_orders(db: Session):
    return db.query(Order).filter(Order.status == "pending").all()

def get_delivered_orders(db: Session):
    return db.query(Order).filter(Order.status == "delivered").all()
