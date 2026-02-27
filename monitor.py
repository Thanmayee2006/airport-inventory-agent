import sqlite3

conn = sqlite3.connect("inventory.db")
cursor = conn.cursor()

# Fetch all items
cursor.execute("SELECT item_name, current_stock, threshold FROM inventory")
items = cursor.fetchall()

print("Checking inventory...\n")

for item in items:
    name = item[0]
    stock = item[1]
    threshold = item[2]

    if stock <= threshold:
        print(f"⚠️ LOW STOCK ALERT: {name}")
        print(f"Current Stock: {stock}")
        print(f"Threshold: {threshold}\n")
    else:
        print(f"✅ {name} stock is sufficient")

conn.close()