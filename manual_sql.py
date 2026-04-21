import sqlite3
import os

db_path = 'db.sqlite3'
print(f"Direct SQLite check on: {os.path.abspath(db_path)}")

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Create table manually if Django is failing
try:
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS core_reportitemevaluation (
        id integer NOT NULL PRIMARY KEY AUTOINCREMENT,
        item_name varchar(500) NOT NULL,
        status varchar(255) NOT NULL,
        report_id bigint NOT NULL REFERENCES core_report (id) DEFERRABLE INITIALLY DEFERRED
    );
    """)
    conn.commit()
    print("Manually created (or confirmed) core_reportitemevaluation")
except Exception as e:
    print(f"Error creating table: {e}")

cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = [t[0] for t in cursor.fetchall()]
print(f"Current tables: {tables}")

with open('manual_sql_output.txt', 'w', encoding='utf-8') as f:
    f.write(f"Tables: {tables}\n")

conn.close()
