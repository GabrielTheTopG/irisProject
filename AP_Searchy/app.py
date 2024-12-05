import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT content FROM papers LIMIT 1')  # Get the first entry from 'papers'
    result = cur.fetchone()
    if result:
        result = result[0]
    else:
        result = "No content found in the database"
    return render_template('searchy.html', result=result)

@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT content FROM papers WHERE content LIKE ?", ('%' + query + '%',))
    result = cur.fetchone()
    if result:
        result = result[0]
    else:
        result = "No content found for the search query"
    return render_template('searchy.html', result=result)

def get_db_connection():
    conn = sqlite3.connect('knowledge_base.db')
    conn.row_factory = sqlite3.Row
    return conn

if __name__ == '__main__':
    from db_module import init_db
    init_db()  # Initialize the database on app startup
    app.run(debug=True)
