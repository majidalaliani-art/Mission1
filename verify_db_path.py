import os
import django
from django.conf import settings
from django.db import connection

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

db_conf = settings.DATABASES['default']
print(f"DATABASE PATH: {db_conf['NAME']}")
print(f"DATABASE ENGINE: {db_conf['ENGINE']}")

with open('db_path_verify.txt', 'w') as f:
    f.write(str(db_conf['NAME']))
