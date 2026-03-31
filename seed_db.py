"""
Seed script to create default users for testing
"""

from database import SessionLocal
from models import User
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

def seed_users():
    db = SessionLocal()
    
    try:
        # Create admin user with custom credentials
        existing_user = db.query(User).filter(User.email == "admin@test.com").first()
        if not existing_user:
            hashed_password = pwd_context.hash("1234")
            admin_user = User(
                email="admin@test.com",
                password=hashed_password
            )
            db.add(admin_user)
            db.commit()
            print("✅ Admin user created!")
            print("   Email: admin@test.com")
            print("   Password: 1234")
        else:
            print("✅ Admin user already exists!")
        
    except Exception as e:
        print(f"❌ Error creating user: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    seed_users()
