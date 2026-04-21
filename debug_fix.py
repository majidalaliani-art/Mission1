import os
import subprocess
import sys

base_dir = r'c:\Users\HP\Desktop\mymission'
python_exe = os.path.join(base_dir, '.venv', 'Scripts', 'python.exe')

def run_cmd(args):
    print(f"Running: {' '.join(args)}")
    result = subprocess.run(args, cwd=base_dir, capture_output=True, text=True)
    if result.stdout: print(f"STDOUT: {result.stdout}")
    if result.stderr: print(f"STDERR: {result.stderr}")
    return result.returncode

# 1. Kill any python processes that might be holding the lock (risky but needed if locked)
# subprocess.run(['taskkill', '/F', '/IM', 'python.exe'], capture_output=True)

# 2. Delete DB
db_path = os.path.join(base_dir, 'db.sqlite3')
if os.path.exists(db_path):
    try:
        os.remove(db_path)
        print("Deleted db.sqlite3")
    except Exception as e:
        print(f"FAILED to delete db.sqlite3: {e}")

# 3. Clean migrations
mig_dir = os.path.join(base_dir, 'core', 'migrations')
for f in os.listdir(mig_dir):
    if f.startswith('0') and f.endswith('.py'):
        try:
            os.remove(os.path.join(mig_dir, f))
            print(f"Deleted {f}")
        except Exception as e:
            print(f"FAILED to delete {f}: {e}")

# 4. Makemigrations
run_cmd([python_exe, 'manage.py', 'makemigrations', 'core'])

# 5. Migrate
run_cmd([python_exe, 'manage.py', 'migrate'])

# 6. Check tables
run_cmd([python_exe, 'manage.py', 'shell', '-c', "from django.db import connection; print('TABLES:', connection.introspection.table_names())"])

# 7. Create Admin
admin_script = "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin123') if not User.objects.filter(username='admin').exists() else print('Admin exists')"
run_cmd([python_exe, 'manage.py', 'shell', '-c', admin_script])
