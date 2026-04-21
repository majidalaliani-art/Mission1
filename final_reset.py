import os
import glob
import subprocess

def run(cmd):
    p = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    print(p.stdout)
    print(p.stderr)

# Delete db
if os.path.exists('db.sqlite3'):
    os.remove('db.sqlite3')

# Delete migrations
for f in glob.glob('core/migrations/0*.py'):
    os.remove(f)

# Run migrations
run('python manage.py makemigrations core')
run('python manage.py migrate')
run('python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser(\'admin\', \'admin@example.com\', \'admin123\') if not User.objects.filter(username=\'admin\').exists() else None"')
