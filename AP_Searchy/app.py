import os
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

DATABASE = 'knowledge_base.db'

# Function to establish a database connection
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# Function to initialize the database using db_module
def init_db():
    from db_module import init_db as db_init  # Import the database initialization function from db_module
    db_init()  # Initialize the database if it does not exist

@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT content FROM papers LIMIT 1')  # Get the first record from the papers table
    result = cur.fetchone()
    conn.close()
    result = result[0] if result else "Keine Inhalte gefunden."
    return render_template('searchy.html', result=result)

@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT content FROM papers WHERE content LIKE ?", ('%' + query + '%',))
    result = cur.fetchone()
    conn.close()
    result = result[0] if result else "Keine Inhalte gefunden."
    return render_template('searchy.html', result=result)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/impressum')
def impressum():
    return render_template('impressum.html')

@app.route('/datenschutz')
def datenschutz():
    return render_template('datenschutz.html')

@app.route('/cookies')
def cookies():
    return render_template('cookies.html')

if __name__ == '__main__':
    init_db()  # Initialize the database on app startup
    app.run(debug=True)
