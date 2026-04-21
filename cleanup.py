import os
import shutil

dir_path = r'c:\Users\HP\Desktop\mymission'
migrations_dir = os.path.join(dir_path, 'core', 'migrations')

# 1. Delete DB
db_path = os.path.join(dir_path, 'db.sqlite3')
if os.path.exists(db_path):
    os.remove(db_path)
    print(f"Deleted {db_path}")

# 2. Delete migration files starting with 0
if os.path.exists(migrations_dir):
    for f in os.listdir(migrations_dir):
        if f.startswith('0'):
            f_path = os.path.join(migrations_dir, f)
            os.remove(f_path)
            print(f"Deleted {f_path}")

# 3. Create Migrations
py_path = r'c:\Users\HP\Desktop\mymission\.venv\Scripts\python.exe'
import subprocess

def run(cmd):
    print(f"Running: {cmd}")
    res = subprocess.run(f'"{py_path}" {cmd}', shell=True, capture_output=True, text=True, cwd=dir_path)
    print(res.stdout)
    print(res.stderr)

run("manage.py makemigrations core")
run("manage.py migrate")
run("manage.py shell -c \"from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin123')\"")
