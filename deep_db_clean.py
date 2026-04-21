import os
import glob
import subprocess
import time

def run_cmd(cmd):
    print(f"Running: {cmd}")
    res = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if res.stdout: print(res.stdout)
    if res.stderr: print(res.stderr)
    return res.returncode

# 1. Delete DB
db_path = r'c:\Users\HP\Desktop\mymission\db.sqlite3'
if os.path.exists(db_path):
    try:
        os.remove(db_path)
        print("Deleted db.sqlite3")
    except Exception as e:
        print(f"Failed to delete db.sqlite3: {e}")

# 2. Delete migrations (keep __init__.py)
migration_pattern = r'c:\Users\HP\Desktop\mymission\core\migrations\0*.py'
migration_files = glob.glob(migration_pattern)
for f in migration_files:
    try:
        os.remove(f)
        print(f"Deleted {f}")
    except Exception as e:
        print(f"Failed to delete {f}: {e}")

time.sleep(1)

# 3. Use absolute path to python
py_path = r'c:\Users\HP\Desktop\mymission\.venv\Scripts\python.exe'

# 4. Run Django commands
run_cmd(f'"{py_path}" manage.py makemigrations core')
run_cmd(f'"{py_path}" manage.py migrate')

# 5. Recreate admin user
create_admin_script = r'c:\Users\HP\Desktop\mymission\create_admin.py'
if os.path.exists(create_admin_script):
    run_cmd(f'"{py_path}" "{create_admin_script}"')
else:
    # Inline create admin if script missing
    run_cmd(f'"{py_path}" manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser(\'admin\', \'admin@example.com\', \'admin123\')"')

print("Sync complete.")
