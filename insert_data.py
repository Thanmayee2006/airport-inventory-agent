import sqlite3

conn = sqlite3.connect("inventory.db")
cursor = conn.cursor()

items = [
    ("Whiskey", "Alcohol", 50, 20, "supplier@example.com"),
    ("Sandwich", "Food", 30, 15, "supplier@example.com"),
    ("Vodka", "Alcohol", 40, 15, "supplier@example.com"),
    ("Wine", "Alcohol", 35, 15, "supplier@example.com"),
    ("Burger", "Food", 25, 10, "supplier@example.com"),
    ("Pasta", "Food", 8, 8, "supplier@example.com"),
    ("Salad", "Food", 18, 7, "supplier@example.com"),
    ("Coffee", "Beverage", 60, 25, "supplier@example.com"),
    ("Tea", "Beverage", 50, 20, "supplier@example.com"),
    ("Orange Juice", "Beverage", 45, 18, "supplier@example.com"),
    ("Soft Drink", "Beverage", 70, 30, "supplier@example.com"),
]

cursor.executemany("""
INSERT INTO inventory (item_name, category, current_stock, threshold, supplier_email)
VALUES (?, ?, ?, ?, ?)
""", items)

conn.commit()
conn.close()

print("Data inserted successfully!")