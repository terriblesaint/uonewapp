import sqlite3
from helpers import connect_to_database
from flask import session
from werkzeug.security import check_password_hash
###
# User Functions
###

# Function to check if username exists and password matches
def login_check_existing_user(username, password):
    conn, cursor = connect_to_database('uonew.db')
    cursor.execute('SELECT * FROM users WHERE username=?', (username,))
    user_data = cursor.fetchone()
    conn.close()
    if user_data and check_password_hash(user_data['password'], password):
        return user_data
    else:
        return None

# Function to check if username exists for registration
def register_check_existing_user(username):
    conn, cursor = connect_to_database('uonew.db')
    cursor.execute('SELECT * FROM users WHERE username=?', (username,))
    user = cursor.fetchone()
    conn.close()
    # Returns True if the username exists, False otherwise
    return user is not None

def get_user_data():
    conn, cursor = connect_to_database('uonew.db')
    user_id = session.get('id')
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    user_data = cursor.fetchone()
    conn.close()
    return user_data

def select_all_users(user_id=None):
    conn, cursor = connect_to_database('uonew.db')
    if user_id:
        cursor.execute("SELECT * FROM users WHERE id =?", (user_id,))
    else:
        cursor.execute("SELECT * FROM users")
    users_data = cursor.fetchall()
    conn.close()
    return users_data