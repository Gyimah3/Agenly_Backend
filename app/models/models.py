from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.orm import Mapped, mapped_column

# class User(Base):
#     __tablename__ = "users"
    
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, index=True)
#     avatar_url = Column(String)
#     email = Column(String, unique=True, index=True)
#     created_at = Column(DateTime, default=datetime.utcnow)
#     updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
#     phone = Column(String)
#     website = Column(String)
#     role = Column(String)
#     permissions = Column(String)  # This should be normalized if possible
#     notifications = Column(Boolean, default=False)

class User(Base):
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, index=True, nullable=False)# Required field
    avatar_url: Mapped[str] = mapped_column(String,nullable=True)# Optional field
    email: Mapped[str] = mapped_column(String, unique=True, index=True, nullable=False)# Required field
    password: Mapped[str] = mapped_column(String,nullable=False)  # Field to store hashed , # Required field
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    phone: Mapped[str] = mapped_column(String,nullable=False)# Required field
    website: Mapped[str] = mapped_column(String,nullable=True)# Optional field
    role: Mapped[str] = mapped_column(String,nullable=True)# Optional field
    permissions: Mapped[str] = mapped_column(String,nullable=True) # Optional field
    notifications: Mapped[bool] = mapped_column(Boolean, default=False)


# class User(Base):
#     __tablename__ = "users"
    
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, index=True, nullable=False)  # Required field
#     avatar_url = Column(String, nullable=True)  # Optional field
#     email = Column(String, unique=True, index=True, nullable=False)  # Required field
#     password = Column(String, nullable=False)  # Required field
#     created_at = Column(DateTime, default=datetime.utcnow)
#     updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
#     phone = Column(String, nullable=False)  # Required field
#     website = Column(String, nullable=True)  # Optional field
#     role = Column(String, nullable=True)  # Optional field
#     permissions = Column(String, nullable=True)  # Optional field
#     notifications = Column(Boolean, default=False)

# class Agent(Base):
#     __tablename__ = "agents"
    
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, index=True)
#     uid = Column(Integer, ForeignKey('users.id'))
#     model = Column(String)
#     prompt_template = Column(String)
#     agent_contact = Column(String)
#     calendly_id = Column(String)
#     db_id = Column(Integer, ForeignKey('database.id'))
#     stage_analyser_template = Column(String)
#     calendly_url = Column(String)
#     iframe_code = Column(String)
#     fb_id = Column(String)
#     whatsapp_id = Column(String)
#     tiktok_id = Column(String)
