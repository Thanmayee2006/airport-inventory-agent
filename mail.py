import sqlite3
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# ✅ Directly define credentials (Simple & Working)
SENDER_EMAIL = "kandariniharika10c11125@gmail.com"
APP_PASSWORD = "myysboetrwxwsmhr"   # 16-character app password (no spaces)


def send_email(to_email, item_name, stock, threshold):
    subject = f"Restock Alert: {item_name}"

    body = f"""
Low Stock Alert!

Item: {item_name}
Current Stock: {stock}
Threshold: {threshold}

Please restock immediately.
"""

    msg = MIMEMultipart()
    msg["From"] = SENDER_EMAIL
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(SENDER_EMAIL, APP_PASSWORD)
        server.send_message(msg)
        server.quit()
        print(f"📧 Email sent for {item_name}")
    except Exception as e:
        print("Email failed:", e)


# ---------------- DATABASE ----------------

conn = sqlite3.connect("inventory.db")
cursor = conn.cursor()

cursor.execute("""
SELECT item_name, current_stock, threshold, supplier_email 
FROM inventory
""")

items = cursor.fetchall()

for name, stock, threshold, email in items:

    if stock <= threshold:
        print(f"⚠️ Low stock detected: {name}")

        # Send email
        send_email(email, name, stock, threshold)

        # Create restock order automatically
        reorder_quantity = threshold * 2

        cursor.execute("""
        INSERT INTO orders (item_name, quantity, status)
        VALUES (?, ?, ?)
        """, (name, reorder_quantity, "Pending"))

        print(f"📝 Order created for {name}")

conn.commit()
conn.close()