import sqlite3
import os

db_path = 'db.sqlite3'
log_file = 'manual_fix_log.txt'

with open(log_file, 'w', encoding='utf-8') as log:
    log.write(f"Connecting to {os.path.abspath(db_path)}\n")
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    
    # Check current tables
    cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = [t[0] for t in cur.fetchall()]
    log.write(f"Current tables: {tables}\n")
    
    if 'core_report' not in tables:
        log.write("Creating core_report...\n")
        cur.execute('''
            CREATE TABLE "core_report" (
                "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
                "region" varchar(100) NOT NULL, 
                "site_type" varchar(100) NULL, 
                "location" varchar(500) NULL, 
                "created_at" datetime NOT NULL, 
                "user_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED
            )
        ''')
    
    if 'core_reportitemevaluation' not in tables:
        log.write("Creating core_reportitemevaluation...\n")
        cur.execute('''
            CREATE TABLE "core_reportitemevaluation" (
                "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
                "item_name" varchar(500) NOT NULL, 
                "status" varchar(255) NOT NULL, 
                "report_id" bigint NOT NULL REFERENCES "core_report" ("id") DEFERRABLE INITIALLY DEFERRED
            )
        ''')
    
    conn.commit()
    
    # Verify again
    cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables_after = [t[0] for t in cur.fetchall()]
    log.write(f"Tables after fix: {tables_after}\n")
    
    conn.close()

print("Manual fix script finished.")
