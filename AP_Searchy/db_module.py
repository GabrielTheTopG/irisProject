import os
import re
import sqlite3
import markdown
import chardet
import time

# Step 1: Set up the Database
def init_db():
    conn = sqlite3.connect('knowledge_base.db')
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
    
    c.execute('CREATE INDEX IF NOT EXISTS idx_paper_content ON papers(content)')
    c.execute('CREATE INDEX IF NOT EXISTS idx_hashtag ON hashtags(hashtag)')
    
    conn.commit()
    conn.close()

def read_file_with_chardet(file_path):
    with open(file_path, 'rb') as f:
        raw_data = f.read()
        result = chardet.detect(raw_data)
        encoding = result['encoding'] if result['confidence'] > 0.5 else 'utf-8'
    
    with open(file_path, 'r', encoding=encoding, errors='replace') as f:
        return f.read()

def import_markdown(directory):
    conn = sqlite3.connect('knowledge_base.db')
    c = conn.cursor()
    
    for subdir, _, files in os.walk(directory):
        directory_name = os.path.basename(subdir)
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(subdir, file)
                try:
                    md_content = read_file_with_chardet(file_path)
                    html_content = markdown.markdown(md_content)
                    
                    c.execute('SELECT id FROM papers WHERE content = ?', (html_content,))
                    if c.fetchone():
                        print(f"Skipping duplicate: {file_path}")
                        continue
                    
                    c.execute('INSERT INTO papers (content, directory_name) VALUES (?, ?)', (html_content, directory_name))
                    paper_id = c.lastrowid
                    
                    hashtags = re.findall(r'#(\w+)', md_content)
                    for tag in hashtags:
                        c.execute('INSERT INTO hashtags (paper_id, hashtag) VALUES (?, ?)', (paper_id, tag))
                    
                    image_matches = re.findall(r'!\[.*\]\((data:image/.+;base64,.+)\)', md_content)
                    for image_data in image_matches:
                        c.execute('INSERT INTO images (paper_id, image_data) VALUES (?, ?)', (paper_id, image_data))
                except Exception as e:
                    print(f"Error processing {file_path}: {e}")
    
    conn.commit()
    conn.close()

# Initialize database and import Markdown files
init_db()
import_markdown('./KnowledgeBase')
