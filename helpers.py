# helpers.py
import sqlite3

# Function to connect to database
def connect_to_database(database_name):
    conn = sqlite3.connect(database_name)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    return conn, cursor