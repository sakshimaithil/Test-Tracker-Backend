from datetime import datetime
from database import Base
from sqlalchemy import Column, Integer, String, DateTime, Float

# ------------------- CLIENT MODEL -------------------
class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, index=True)
    client_name = Column(String)
    company_name = Column(String)
    email = Column(String, nullable=True)
    phone = Column(String)

    status = Column(String, default="new")

    meeting_date = Column(String)
    follow_up_date = Column(String)

    notes = Column(String)
    meeting_done_by = Column(String)

    deal_value = Column(Float)
    assigned_to = Column(String)

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


# ------------------- USER MODEL -------------------
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)