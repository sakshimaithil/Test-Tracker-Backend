from database import engine
from models import Base

# Drop all existing tables
print("🗑️ Dropping existing tables...")
Base.metadata.drop_all(bind=engine)

# Recreate all tables fresh
print("✅ Creating new tables...")
Base.metadata.create_all(bind=engine)

print("✅ Database reset complete! The unique constraint on email has been removed.")
