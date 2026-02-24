# #Database Connection Settings
# import psycopg2


# def connection():
#     con = psycopg2.connect(
#         host="localhost",
#         database="ecommerce",
#         user="postgres",
#         password="dev",
#         port="5432"
#     )

#     if con:
#         print("Connention successful")
#     else:
#         print("Connection failed")
#     return con

# conn = connection()

# import psycopg2
# import streamlit as st

# def connection():
#     try:
#         con = psycopg2.connect(
#             host=st.secrets["DB_HOST"],
#             database=st.secrets["DB_NAME"],
#             user=st.secrets["DB_USER"],
#             password=st.secrets["DB_PASSWORD"],
#             port=st.secrets["DB_PORT"],
#             sslmode="require"
#         )
#         return con
#     except Exception as e:
#         st.error(f"Database connection failed: {e}")
#         return None

# conn = connection()

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
