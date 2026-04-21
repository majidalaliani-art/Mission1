import os
import django
from django.db import connection

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

print("Current tables in DB:")
print(connection.introspection.table_names())

if 'core_reportitemevaluation' in connection.introspection.table_names():
    print("SUCCESS: core_reportitemevaluation exists.")
else:
    print("FAILURE: core_reportitemevaluation is missing.")
