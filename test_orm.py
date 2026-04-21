import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth.models import User
from core.models import Report, ReportItemEvaluation

try:
    user = User.objects.first()
    if not user:
        print("No users found. Creating superuser.")
        user = User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
    
    report = Report.objects.create(user=user, region='الملز')
    item = ReportItemEvaluation.objects.create(report=report, item_name='Test Item', status='Pass')
    print(f"SUCCESS: Record created! ID: {item.id}")
    item.delete()
    report.delete()
except Exception as e:
    import traceback
    print(f"FAILURE: {e}")
    traceback.print_exc()
