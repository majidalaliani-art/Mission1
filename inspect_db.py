import os
import sqlite3
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

db_path = 'db.sqlite3'
print(f"Inspecting DB at: {os.path.abspath(db_path)}")

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Get tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = [t[0] for t in cursor.fetchall()]

# Get migration history
try:
    cursor.execute("SELECT app, name FROM django_migrations")
    migrations = cursor.fetchall()
except Exception as e:
    migrations = str(e)

conn.close()

output = f"Tables: {tables}\nMigrations: {migrations}\n"
with open('inspect_result.txt', 'w', encoding='utf-8') as f:
    f.write(output)
print("Result written to inspect_result.txt")
