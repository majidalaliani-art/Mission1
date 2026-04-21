import os
import shutil
import glob
import subprocess
import sys

def run(cmd):
    print(f"Running: {cmd}")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
    else:
        print(result.stdout)

base_dir = os.getcwd()
migrations_dir = os.path.join(base_dir, 'core', 'migrations')
db_path = os.path.join(base_dir, 'db.sqlite3')
py_path = os.path.join(base_dir, '.venv', 'Scripts', 'python.exe')

# 1. Clean migrations
if os.path.exists(migrations_dir):
    files = glob.glob(os.path.join(migrations_dir, '0*.py'))
    for f in files:
        os.remove(f)
        print(f"Deleted {f}")

# 2. Clean DB
if os.path.exists(db_path):
    os.remove(db_path)
    print(f"Deleted {db_path}")

# 3. Makemigrations
run(f'"{py_path}" manage.py makemigrations core')

# 4. Migrate
run(f'"{py_path}" manage.py migrate')

# 5. Create Superuser (admin / admin123)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
import django
django.setup()
from django.contrib.auth.models import User
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
    print("Superuser created: admin / admin123")
else:
    print("Superuser admin already exists")
