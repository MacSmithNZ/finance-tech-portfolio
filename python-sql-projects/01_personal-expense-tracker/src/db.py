# src/db.py
import sqlite3
import os

# Ensure the data folder exists
os.makedirs("data", exist_ok=True)

# Connect to SQLite database (creates file if it doesn't exist)
DB_PATH = "data/expenses.db"
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# -------------------------------
# Create tables
# -------------------------------

# Categories table
cursor.execute("""
CREATE TABLE IF NOT EXISTS categories (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE
)
""")

# Payment Methods table
cursor.execute("""
CREATE TABLE IF NOT EXISTS payment_methods (
    payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    method TEXT NOT NULL UNIQUE
)
""")

# Expenses table
cursor.execute("""
CREATE TABLE IF NOT EXISTS expenses (
    expense_id INTEGER PRIMARY KEY AUTOINCREMENT,
    date DATE NOT NULL,
    amount DECIMAL(10,2) NOT NULL,
    category_id INTEGER,
    payment_id INTEGER,
    note TEXT,
    FOREIGN KEY (category_id) REFERENCES categories (category_id),
    FOREIGN KEY (payment_id) REFERENCES payment_methods (payment_id)
)
""")

# Commit changes and close connection
conn.commit()
conn.close()

print(f"Database created at {DB_PATH} with tables: categories, payment_methods, expenses")