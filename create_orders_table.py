import sqlite3

conn = sqlite3.connect("inventory.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    item_name TEXT,
    order_quantity INTEGER,
    order_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    status TEXT
)
""")

conn.commit()
conn.close()

print("Orders table created successfully!")