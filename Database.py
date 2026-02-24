
import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "inventory.db")

def connection():
    try:
        con = sqlite3.connect(DB_PATH, check_same_thread=False)
        return con
    except Exception as e:
        print("DB Connection Error:", e)
        return None

conn = connection()
# ----------------------------
# CREATE TABLES IF NOT EXIST
# ----------------------------
def init_db():
    if conn is None:
        return
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        price REAL,
        quantity INTEGER
    )
    """)

    conn.commit()

# Run at import time
init_db()



