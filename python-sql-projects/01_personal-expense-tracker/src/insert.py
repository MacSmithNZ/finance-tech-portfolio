import sqlite3
from datetime import date

DB_PATH = "data/expenses.db"

# -------------------------------
# Helper function to connect
# -------------------------------
def get_connection():
    conn = sqlite3.connect(DB_PATH)
    return conn, conn.cursor()

# -------------------------------
# Insert a new category
# -------------------------------
def add_category(name):
    conn, cursor = get_connection()
    cursor.execute("INSERT OR IGNORE INTO categories (name) VALUES (?)", (name,))
    conn.commit()
    conn.close()
    print(f"Category '{name}' added.")
    
# -------------------------------
# Insert a new payment method
# -------------------------------
def add_payment_method(method):
    conn, cursor = get_connection()
    cursor.execute("INSERT OR IGNORE INTO payment_methods (method) VALUES (?)", (method,))
    conn.commit()
    conn.close()
    print(f"Payment method '{method}' added.")
    
# -------------------------------
# Insert a new expense
# -------------------------------
def add_expense(amount, category_name, payment_method, expense_date=None, note=None):
    if expense_date is None:
        expense_date = date.today().isoformat() # Default to today
        
    conn, cursor = get_connection()
    
    cursor.execute("""
    INSERT INTO expenses (date, amount, category_id, payment_id, note)
    VALUES (?, ?, 
        (SELECT category_id FROM categories WHERE name=?),
        (SELECT payment_id FROM payment_methods WHERE method=?),
        ?)
    """, (expense_date, amount, category_name, payment_method, note))
    
    conn.commit()
    conn.close()
    print(f"Expense added: {amount} on {expense_date} ({category_name}, {payment_method})")