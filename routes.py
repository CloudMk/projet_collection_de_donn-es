from flask import Flask, render_template, request, jsonify
import sqlite3
from sqlite3 import Error

app = Flask(__name__)

# Initialize SQLite database
def init_db():
    try:
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS submissions (
                     id INTEGER PRIMARY KEY AUTOINCREMENT,
                     name TEXT NOT NULL,
                     email TEXT NOT NULL
                     )''')
        conn.commit()
        conn.close()
    except Error as e:
        print(f"Error initializing database: {e}")

# Call init_db when the app starts
init_db()

@app.route('/')
def welcom():
    return render_template('view/welcome.html')

@app.route('/auth')
def index():
    return render_template('view/auth.html')