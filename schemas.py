from pydantic import BaseModel, EmailStr
from typing import Optional

class ClientCreate(BaseModel):
    client_name: str
    company_name: str
    email: str
    phone: str
    status: str
    meeting_date: str
    follow_up_date: str
    notes: str
    meeting_done_by: str
    deal_value: float
    assigned_to: str

class UserRegister(BaseModel):
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"

class RegisterResponse(BaseModel):
    message: str