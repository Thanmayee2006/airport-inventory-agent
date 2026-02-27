import streamlit as st
import sqlite3
import smtplib
import pandas as pd
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

st.set_page_config(page_title="Airport Lounge Inventory", page_icon="✈️", layout="wide")

st.title("✈️ Airport Lounge Inventory System")

# ---------------- DATABASE CONNECTION ----------------
def get_connection():
    return sqlite3.connect("inventory.db")

# ---------------- FETCH INVENTORY ----------------
def get_inventory():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, item_name, category, current_stock, threshold, supplier_email FROM inventory")
    data = cursor.fetchall()
    conn.close()
    return data

# ---------------- UPDATE STOCK ----------------
def update_stock(item_name, quantity):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE inventory SET current_stock = current_stock - ? WHERE item_name = ?", (quantity, item_name))
    conn.commit()
    conn.close()

# ---------------- EMAIL FUNCTION ----------------
def send_email(to_email, item_name, stock, threshold):
    sender = "kandariniharika10c11125@gmail.com"
    password = "myysboetrwxwsmhr"
    subject = f"Restock Alert: {item_name}"
    body = f"""Low Stock Alert!

Item: {item_name}
Current Stock: {stock}
Threshold: {threshold}

Please restock immediately."""
    
    msg = MIMEMultipart()
    msg["From"] = sender
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))
    
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender, password)
        server.send_message(msg)
        server.quit()
    except Exception as e:
        st.error(f"Email failed: {e}")

# ---------------- CHECK LOW STOCK ----------------
def check_low_stock():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT item_name, current_stock, threshold, supplier_email FROM inventory")
    items = cursor.fetchall()

    for name, stock, threshold, email in items:
        if stock <= threshold:
            st.error(f"⚠️ Low Stock: {name}")
            cursor.execute("SELECT * FROM orders WHERE item_name = ? AND status = 'Pending'", (name,))
            existing_order = cursor.fetchone()

            if not existing_order:
                send_email(email, name, stock, threshold)
                reorder_quantity = threshold * 2
                cursor.execute("INSERT INTO orders (item_name, order_quantity, status) VALUES (?, ?, ?)", 
                             (name, reorder_quantity, "Pending"))
                conn.commit()
                st.success(f"📝 Order created for {name}")
            else:
                st.info(f"📦 Pending order already exists for {name}")

    conn.close()

# ---------------- FETCH COMPLETED ORDERS ----------------
def get_completed_orders():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM orders WHERE status = 'Completed'")
    orders = cursor.fetchall()
    cursor.close()
    conn.close()
    return orders

# ---------------- UI ----------------
data = get_inventory()

st.subheader("📦 Inventory Status")

if data:
    df = pd.DataFrame(data, columns=["ID", "Item", "Category", "Stock", "Threshold", "Supplier Email"])
    
    for idx, row in df.iterrows():
        col1, col2, col3, col4 = st.columns([3, 2, 1, 2])
        
        with col1:
            st.markdown(f"**{row['Item']}**")
            st.caption(f"Category: {row['Category']}")
        
        with col2:
            st.metric("Stock", row['Stock'])
        
        with col3:
            st.metric("Threshold", row['Threshold'])
        
        with col4:
            if row['Stock'] <= row['Threshold']:
                st.error("⚠️ Low Stock")
            else:
                st.success("✅ In Stock")
        
        st.divider()
else:
    st.info("No inventory items found.")

st.subheader("🛒 Process Sale")

col1, col2, col3 = st.columns([2, 1, 1])

with col1:
    item_names = [row[1] for row in data] if data else []
    selected_item = st.selectbox("Select Item", item_names)

with col2:
    quantity = st.number_input("Quantity", min_value=1, value=1)

with col3:
    st.write("")
    st.write("")
    if st.button("Process Sale", type="primary", use_container_width=True):
        update_stock(selected_item, quantity)
        st.success(f"✅ Sold {quantity} unit(s) of {selected_item}")
        check_low_stock()
        st.rerun()

# ---------------- COMPLETED ORDERS SECTION ----------------
st.subheader("📋 Completed Orders")

orders_data = get_completed_orders()

if orders_data:
    orders_df = pd.DataFrame(orders_data, columns=["Order ID", "Item Name", "Quantity", "Order Date", "Status"])
    orders_df = orders_df[["Order ID", "Item Name", "Quantity", "Order Date"]]
    st.dataframe(orders_df, use_container_width=True, hide_index=True)
else:
    st.info("No completed orders found.")
