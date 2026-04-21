import os
import shutil
import subprocess

# Define paths
base_dir = r'c:\Users\HP\Desktop\mymission'
db_path = os.path.join(base_dir, 'db.sqlite3')
migrations_dir = os.path.join(base_dir, 'core', 'migrations')

print(f"Cleaning up in {base_dir}...")

# 1. Delete db.sqlite3
if os.path.exists(db_path):
    try:
        os.remove(db_path)
        print("db.sqlite3 deleted.")
    except Exception as e:
        print(f"Error deleting db.sqlite3: {e}")

# 2. Delete all migration files except __init__.py
if os.path.exists(migrations_dir):
    for f in os.listdir(migrations_dir):
        if f.startswith('0') and f.endswith('.py'):
            p = os.path.join(migrations_dir, f)
            try:
                os.remove(p)
                print(f"Deleted migration: {f}")
            except Exception as e:
                print(f"Error deleting {f}: {e}")

# 3. Create fresh migrations
print("Running makemigrations...")
subprocess.run([r'.\.venv\Scripts\python.exe', 'manage.py', 'makemigrations', 'core'], cwd=base_dir)

# 4. Migrate
print("Running migrate...")
subprocess.run([r'.\.venv\Scripts\python.exe', 'manage.py', 'migrate'], cwd=base_dir)

# 5. Create superuser
print("Creating superuser...")
shell_cmd = "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin123')"
subprocess.run([r'.\.venv\Scripts\python.exe', 'manage.py', 'shell', '-c', shell_cmd], cwd=base_dir)

print("Done!")
