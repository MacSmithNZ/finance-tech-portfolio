import sqlite3
import pandas as pd

DB_PATH = "data/expenses.db"

# -------------------------------
# Helper function to connect
# -------------------------------
def get_connection():
    conn = sqlite3.connect(DB_PATH)
    return conn, conn.cursor()

# -------------------------------
# 1. Total expenses
# -------------------------------
def total_expenses():
    conn, cursor = get_connection()
    cursor.execute("SELECT SUM(amount) FROM expenses")
    total = cursor.fetchone()[0]
    conn.close()
    return total if total is not None else 0

# -------------------------------
# 2. Monthly expenses
# -------------------------------
def monthly_expenses():
    conn = sqlite3.connect(DB_PATH)
    query = """
    SELECT strftime('%Y-%m', e.date) AS month, SUM(e.amount) AS total
    FROM expenses e
    GROUP BY month
    ORDER BY month
    """
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

# -------------------------------
# Expenses_by_category
# -------------------------------
def expenses_by_category():
    conn = sqlite3.connect(DB_PATH)
    query = """
    SELECT c.name AS category, SUM(e.amount) AS total
    FROM expenses e
    JOIN categories c ON e.category_id = c.category_id
    GROUP BY c.name
    ORDER BY total DESC
    """
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

# -------------------------------
# Expenses by payment method
# -------------------------------
def expenses_by_payment_method():
    conn = sqlite3.connect(DB_PATH)
    query = """
    SELECT p.method AS payment_method, SUM(e.amount) AS total
    FROM expenses e
    JOIN payment_methods p ON e.payment_id = p.payment_id
    GROUP BY p.method
    ORDER BY total DESC
    """
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

# -------------------------------
# 5. Recent expenses
# -------------------------------
def recent_expenses(limit=10):
    conn = sqlite3.connect(DB_PATH)
    query = f"""
    SELECT e.date, e.amount, c.name AS category, p.method AS payment_method, e.note
    FROM expenses e
    LEFT JOIN categories c ON e.category_id = c.category_id
    LEFT JOIN payment_methods p ON e.payment_id = p.payment_id
    ORDER BY e.date DESC
    LIMIT {limit}
    """
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df