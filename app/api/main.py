# # /backend/app/main.py

# from fastapi import FastAPI
# from app.api.endpoints import users

# app = FastAPI()

# #app.include_router(items.router, prefix="/api/v1", tags=["items"])
# app.include_router(users.router, prefix="/api/v1", tags=["users"])
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

# Import routers from your endpoint modules
from app.api.endpoints import user  # Adjust imports according to your project structure

# Import database session utility (if you've structured it this way)
from app.database import engine, Base
from app.models import models  # This imports models to ensure they are known to SQLAlchemy
from app.core.config import settings  # Assuming your settings include CORS origins, etc.

# Initialize FastAPI app
app = FastAPI(title="Agenly", version="1.0.0")

# Setup Middleware, e.g., CORS
origins = [
    "http://localhost:3000",  # Adjust this list based on your front-end URLs
    "https://yourproductiondomain.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create database tables (if not already existing)
Base.metadata.create_all(bind=engine)

# Include routers from your endpoints modules
app.include_router(user.router, prefix="/api/v1/users", tags=["users"])
#app.include_router(agent.router, prefix="/api/v1/agents", tags=["agents"])

# You might also want to add a root endpoint for basic API health check
@app.get("/")
def read_root():
    return {"message": "Welcome to your FastAPI application!"}

