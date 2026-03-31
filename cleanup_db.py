from database import engine

# Drop the users table if it exists (from old backend)
with engine.connect() as connection:
    connection.execute("DROP TABLE IF EXISTS users CASCADE")
    connection.commit()
    print("✅ Dropped users table (old backend)")

print("✅ Cleanup complete! Only 'clients' table should remain.")
