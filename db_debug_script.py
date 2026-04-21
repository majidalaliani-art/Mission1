import os
import sqlite3
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.db import connection

db_path = 'db.sqlite3'
abs_path = os.path.abspath(db_path)

with open('db_debug.txt', 'w', encoding='utf-8') as f:
    f.write(f"Absolute DB path: {abs_path}\n")
    f.write(f"File size: {os.path.getsize(db_path) if os.path.exists(db_path) else 'NOT FOUND'}\n")
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = [t[0] for t in cursor.fetchall()]
    f.write(f"Tables index: {tables}\n\n")
    
    for table in tables:
        cursor.execute(f"PRAGMA table_info({table})")
        columns = cursor.fetchall()
        f.write(f"Table: {table}\n")
        f.write(f"Columns: {columns}\n\n")
    
    conn.close()

print("Debug info written to db_debug.txt")
