import os
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

DATABASE = 'knowledge_base.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    if not os.path.exists(DATABASE):
        conn = sqlite3.connect(DATABASE)
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS papers (
                        id INTEGER PRIMARY KEY,
                        content TEXT,
                        directory_name TEXT
                    )''')
        c.execute('''CREATE TABLE IF NOT EXISTS hashtags (
                        id INTEGER PRIMARY KEY,
                        paper_id INTEGER,
                        hashtag TEXT,
                        FOREIGN KEY (paper_id) REFERENCES papers (id)
                    )''')
        c.execute('''CREATE TABLE IF NOT EXISTS images (
                        id INTEGER PRIMARY KEY,
                        paper_id INTEGER,
                        image_data TEXT,
                        FOREIGN KEY (paper_id) REFERENCES papers (id)
                    )''')
        conn.commit()
        conn.close()

@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT content FROM papers LIMIT 1')
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

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
