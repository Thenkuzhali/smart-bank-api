import sqlite3

# Connect to your existing database file
conn = sqlite3.connect("smart_bank.db")
cursor = conn.cursor()

# Step 1: Add columns as nullable (no default)
cursor.execute("ALTER TABLE users ADD COLUMN created_at DATETIME;")
cursor.execute("ALTER TABLE users ADD COLUMN updated_at DATETIME;")

# Step 2: Fill existing rows with current timestamp
cursor.execute("UPDATE users SET created_at = CURRENT_TIMESTAMP WHERE created_at IS NULL;")
cursor.execute("UPDATE users SET updated_at = CURRENT_TIMESTAMP WHERE updated_at IS NULL;")

# Commit and close
conn.commit()
conn.close()

print("Columns added and updated successfully!")