import sqlite3
import os

db_path = 'db.sqlite3'
out_file = 'lite_check.txt'

try:
    if not os.path.exists(db_path):
        result = f"Error: {db_path} does not exist."
    else:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = [t[0] for t in cursor.fetchall()]
        conn.close()
        result = f"Tables in {db_path}: {tables}"
except Exception as e:
    result = f"Error: {str(e)}"

with open(out_file, 'w', encoding='utf-8') as f:
    f.write(result)
