import os
import re
import sqlite3
import markdown
import chardet
import time

# Step 1: Set up the Database
def init_db():
    # Connect to the SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect('knowledge_base.db')
    c = conn.cursor()
    
    # Create tables for storing papers, hashtags, and images
    c.execute('''CREATE TABLE IF NOT EXISTS papers (
                    id INTEGER PRIMARY KEY,
                    content TEXT UNIQUE,  -- Ensure content is unique
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
    
    # Add indexes for faster search performance
    c.execute('CREATE INDEX IF NOT EXISTS idx_paper_content ON papers(content)')
    c.execute('CREATE INDEX IF NOT EXISTS idx_hashtag ON hashtags(hashtag)')
    
    # Commit changes and close the connection
    conn.commit()
    conn.close()


# Step 2: Import Markdown Files into Database with encoding handling
def read_file_with_chardet(file_path):
    # Open the file in binary mode to detect encoding using chardet
    with open(file_path, 'rb') as f:
        raw_data = f.read()
        # Detect encoding of the file with chardet, defaulting to 'utf-8' if confidence is low
        result = chardet.detect(raw_data)
        encoding = result['encoding'] if result['confidence'] > 0.5 else 'utf-8'
        print(f"Detected encoding for {file_path}: {encoding} (Confidence: {result['confidence']})")
    
    # Open the file with detected encoding and handle any unreadable characters with 'replace'
    with open(file_path, 'r', encoding=encoding, errors='replace') as f:
        return f.read()

def import_markdown(directory):
    # Connect to the SQLite database
    conn = sqlite3.connect('knowledge_base.db')
    c = conn.cursor()
    
    # Walk through each subdirectory and file in the specified directory
    for subdir, _, files in os.walk(directory):
        directory_name = os.path.basename(subdir)
        for file in files:
            # Only process Markdown files
            if file.endswith('.md'):
                file_path = os.path.join(subdir, file)
                print(f"Processing file: {file_path}")  # Track progress
                try:
                    start_time = time.time()
                    
                    # Read file content using the custom function with chardet
                    md_content = read_file_with_chardet(file_path)
                    # Convert Markdown content to HTML for storage
                    html_content = markdown.markdown(md_content)
                    
                    # Use INSERT OR IGNORE to skip duplicates automatically
                    c.execute('INSERT OR IGNORE INTO papers (content, directory_name) VALUES (?, ?)', (html_content, directory_name))
                    if c.rowcount == 0:  # Check if the insert was ignored (duplicate)
                        print(f"Skipping duplicate: {file_path}")
                        continue
                    
                    paper_id = c.lastrowid
                    
                    # Extract hashtags using a regex and store them in the hashtags table
                    hashtags = re.findall(r'#(\w+)', md_content)
                    for tag in hashtags:
                        c.execute('INSERT INTO hashtags (paper_id, hashtag) VALUES (?, ?)', (paper_id, tag))
                    
                    # Extract images in base64 format from the Markdown content and store them
                    image_matches = re.findall(r'!\[.*\]\((data:image/.+;base64,.+)\)', md_content)
                    for image_data in image_matches:
                        c.execute('INSERT INTO images (paper_id, image_data) VALUES (?, ?)', (paper_id, image_data))
                    
                    # Log the processing time for each file
                    print(f"Processed {file_path} in {time.time() - start_time:.2f} seconds.")
                
                except Exception as e:
                    # Print any errors encountered during file processing
                    print(f"Error processing file {file_path}: {e}")
    
    # Commit changes and close the connection
    conn.commit()
    conn.close()

# Initialize the database and import Markdown files
if __name__ == "__main__":
    init_db()
    import_markdown('./KnowledgeBase')
