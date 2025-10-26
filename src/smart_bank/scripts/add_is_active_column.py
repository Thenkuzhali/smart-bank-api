import sqlite3

# Connect to your existing database
conn = sqlite3.connect("smart_bank.db")
cursor = conn.cursor()

try:
    cursor.execute("ALTER TABLE users ADD COLUMN is_active BOOLEAN DEFAULT 1;")
    print("✅ 'is_active' column added successfully!")
except sqlite3.OperationalError as e:
    print(f"⚠️ Skipping: {e}")

conn.commit()
conn.close()