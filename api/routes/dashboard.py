from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.database.connection import get_db
from api.crud.dashboard import  get_latest_orders,get_orders_delivered_on_20_feb,get_last_month_revenue,get_last_3_months_revenue,get_delivered_orders,get_pending_orders
router = APIRouter()
@router.get("/analytics")
def get_dashboard_analytics(db: Session = Depends(get_db)):
    return {
        "latest_orders": get_latest_orders(db),
        "last_month_revenue": get_last_month_revenue(db),
        "orders_delivered_on_20_feb": get_orders_delivered_on_20_feb(db),
        "last_3_months_revenue": get_last_3_months_revenue(db),
        "pending_orders": get_pending_orders(db),
        "delivered_orders": get_delivered_orders(db),
    }