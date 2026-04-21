import os
import sqlite3
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

db_path = 'db.sqlite3'
print(f"Checking DB at: {os.path.abspath(db_path)}")

conn = sqlite3.connect(db_path)
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = [t[0] for t in cursor.fetchall()]
conn.close()

with open('db_status.txt', 'w', encoding='utf-8') as f:
    f.write(f"DB Path: {os.path.abspath(db_path)}\n")
    f.write(f"Tables found: {tables}\n")
    if 'core_reportitemevaluation' in tables:
        f.write("RESULT: TABLE EXISTS\n")
    else:
        f.write("RESULT: TABLE MISSING\n")
