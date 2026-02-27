import sqlite3

# Connect to database (creates file if not exists)
conn = sqlite3.connect("inventory2.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE inventory2 (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    item_name TEXT NOT NULL,
    category TEXT,
    current_stock INTEGER,
    threshold INTEGER,
    supplier_email TEXT
)
""")

# Insert sample data
cursor.execute("""
INSERT INTO inventory2 (item_name, category, current_stock, threshold, supplier_email)
VALUES (?, ?, ?, ?, ?)
""", ("Whiskey", "Alcohol", 50, 20, "supplier@example.com"))

cursor.execute("""
INSERT INTO inventory2 (item_name, category, current_stock, threshold, supplier_email)
VALUES (?, ?, ?, ?, ?)
""", ("Sandwich", "Food", 30, 15, "supplier@example.com"))

# More Alcohol
cursor.execute("""
INSERT INTO inventory2 (item_name, category, current_stock, threshold, supplier_email)
VALUES (?, ?, ?, ?, ?)
""", ("Vodka", "Alcohol", 40, 15, "supplier@example.com"))

cursor.execute("""
INSERT INTO inventory2 (item_name, category, current_stock, threshold, supplier_email)
VALUES (?, ?, ?, ?, ?)
""", ("Wine", "Alcohol", 35, 15, "supplier@example.com"))

# More Food
cursor.execute("""
INSERT INTO inventory2 (item_name, category, current_stock, threshold, supplier_email)
VALUES (?, ?, ?, ?, ?)
""", ("Burger", "Food", 25, 10, "supplier@example.com"))

cursor.execute("""
INSERT INTO inventory2 (item_name, category, current_stock, threshold, supplier_email)
VALUES (?, ?, ?, ?, ?)
""", ("Pasta", "Food", 20, 8, "supplier@example.com"))

cursor.execute("""
INSERT INTO inventory2 (item_name, category, current_stock, threshold, supplier_email)
VALUES (?, ?, ?, ?, ?)
""", ("Salad", "Food", 18, 7, "supplier@example.com"))

# Beverages
cursor.execute("""
INSERT INTO inventory2 (item_name, category, current_stock, threshold, supplier_email)
VALUES (?, ?, ?, ?, ?)
""", ("Coffee", "Beverage", 60, 25, "supplier@example.com"))

cursor.execute("""
INSERT INTO inventory2 (item_name, category, current_stock, threshold, supplier_email)
VALUES (?, ?, ?, ?, ?)
""", ("Tea", "Beverage", 50, 20, "supplier@example.com"))

cursor.execute("""
INSERT INTO inventory2 (item_name, category, current_stock, threshold, supplier_email)
VALUES (?, ?, ?, ?, ?)
""", ("Orange Juice", "Beverage", 45, 18, "supplier@example.com"))

cursor.execute("""
INSERT INTO inventory2 (item_name, category, current_stock, threshold, supplier_email)
VALUES (?, ?, ?, ?, ?)
""", ("Soft Drink", "Beverage", 70, 30, "supplier@example.com"))


# Save changes
conn.commit()

conn.close()

print("Database created and data inserted successfully!")