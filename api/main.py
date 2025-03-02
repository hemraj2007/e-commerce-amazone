from fastapi import FastAPI
from api.routes import auth, users,category,product,address,cart,review,order,dashboard
from api.database.connection import engine
from api.database.base import Base

# Create database tables if they don't exist
Base.metadata.create_all(bind=engine)


# Initialize FastAPI app
app = FastAPI()

# Include authentication-related routes
app.include_router(auth.router, prefix="/auth", tags=["Auth"])

# Include user-related routes
app.include_router(users.router, prefix="/users", tags=["Users"])

# Include produt-related routes
app.include_router(category.router, prefix="/category", tags=["Category"])

# Include produt-related routes
app.include_router(product.router, prefix="/product", tags=["Product"])

# Include produt-related routes
app.include_router(address.router, prefix="/address", tags=["Address"])

# Include produt-related routes
app.include_router(cart.router, prefix="/cart", tags=["Cart"])

# Include produt-related routes
app.include_router(order.router, prefix="/order", tags=["Order"])

# Include produt-related routes
app.include_router(review.router, prefix="/review", tags=["Review"])

app.include_router(dashboard.router, prefix="/dashboard", tags=["Dashboard"])