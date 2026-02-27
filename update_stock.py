import sqlite3

conn = sqlite3.connect("inventory.db")
cursor = conn.cursor()

# Example: reduce Coffee stock by 5
cursor.execute("""
UPDATE inventory
SET current_stock = current_stock - ?
WHERE item_name = ?
""", (5, "Coffee"))

conn.commit()
conn.close()

print("Stock updated successfully!")