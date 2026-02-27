import sqlite3

conn = sqlite3.connect("inventory.db")
cursor = conn.cursor()

# Create table (safe version)
cursor.execute("""
CREATE TABLE IF NOT EXISTS inventory (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    item_name TEXT NOT NULL,
    category TEXT,
    current_stock INTEGER,
    threshold INTEGER,
    supplier_email TEXT
)
""")

conn.commit()
conn.close()

print("Table created successfully!")