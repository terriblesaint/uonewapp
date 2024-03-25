import sqlite3
from helpers import connect_to_database


# Function to get link info
def select_links():
    conn, cursor = connect_to_database('uonew.db')
    cursor.execute("SELECT * FROM mclinks")
    links_data = cursor.fetchall()
    conn.close()
    return links_data