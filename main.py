from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from database import engine, SessionLocal
import models

from models import Client
from schemas import ClientCreate

# ✅ JWT imports
from auth.dependencies import get_current_user
from auth.auth_routes import router as auth_router, get_db

# Create tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# ✅ Auth routes include
app.include_router(auth_router, prefix="/api/auth")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root
@app.get("/")
def root():
    return {"message": "CRM Backend is running 🚀"}

# ------------------- GET ALL CLIENTS -------------------
@app.get("/api/clients")
def get_clients(
    db: Session = Depends(get_db),
    user=Depends(get_current_user)   # 🔐 PROTECTED
):
    return db.query(Client).all()

# ------------------- CREATE CLIENT -------------------
@app.post("/api/clients")
def create_client(
    client: ClientCreate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)   # 🔐 PROTECTED
):
    new_client = Client(
        client_name=client.client_name,
        company_name=client.company_name,
        email=client.email,
        phone=client.phone,
        status=client.status,
        meeting_date=client.meeting_date,
        follow_up_date=client.follow_up_date,
        notes=client.notes,
        meeting_done_by=client.meeting_done_by,
        deal_value=client.deal_value,
        assigned_to=client.assigned_to,
    )

    db.add(new_client)
    db.commit()
    db.refresh(new_client)
    return new_client

# ------------------- GET CLIENT BY ID -------------------
@app.get("/api/clients/{client_id}")
def get_client(
    client_id: int,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)   # 🔐 PROTECTED
):
    client = db.query(Client).filter(Client.id == client_id).first()

    if not client:
        raise HTTPException(status_code=404, detail="Client not found")

    return client

# ------------------- UPDATE CLIENT -------------------
@app.put("/api/clients/{client_id}")
def update_client(
    client_id: int,
    client: ClientCreate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)   # 🔐 PROTECTED
):
    db_client = db.query(Client).filter(Client.id == client_id).first()

    if not db_client:
        raise HTTPException(status_code=404, detail="Client not found")

    db_client.client_name = client.client_name
    db_client.company_name = client.company_name
    db_client.email = client.email
    db_client.phone = client.phone
    db_client.status = client.status
    db_client.meeting_date = client.meeting_date
    db_client.follow_up_date = client.follow_up_date
    db_client.notes = client.notes
    db_client.meeting_done_by = client.meeting_done_by
    db_client.deal_value = client.deal_value
    db_client.assigned_to = client.assigned_to

    db.commit()
    db.refresh(db_client)
    return db_client

# ------------------- DELETE CLIENT -------------------
@app.delete("/api/clients/{client_id}")
def delete_client(
    client_id: int,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)   # 🔐 PROTECTED
):
    db_client = db.query(Client).filter(Client.id == client_id).first()

    if not db_client:
        raise HTTPException(status_code=404, detail="Client not found")

    db.delete(db_client)
    db.commit()

    return {"detail": "Client deleted"}