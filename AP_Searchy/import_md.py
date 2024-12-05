import os
import sqlite3
import markdown
import chardet

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
                    print(f"Processing file: {file_path}") 
                    md_content = read_file_with_chardet(file_path)
                    html_content = markdown.markdown(md_content)
                    c.execute('SELECT id FROM papers WHERE content = ?', (html_content,))
                    if not c.fetchone():
                        print(f"Inserting new content from {file_path}")
                        c.execute('INSERT INTO papers (content, directory_name) VALUES (?, ?)', (html_content, directory_name))
                except Exception as e:
                    print(f"Error processing file: {file_path} - {e}")
    conn.commit()
    conn.close()

if __name__ == "__main__":
    import_markdown('./KnowledgeBase')
