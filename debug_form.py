import os
import django
import json
import sys

try:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    django.setup()
    from core.forms import ReportForm
    print("Django setup successful.")
except Exception as e:
    print(f"Django setup failed: {e}")
    sys.exit(1)

# Simulate the data sent by the Wizard
data = {
    'region': 'العليا',
    'site_type': 'مواقع',
    'location': 'حديقة المصيف',
    'evaluation_data': json.dumps({'أعمال النظافة': 'منفذ'}),
    'note': 'Test note'
}

form = ReportForm(data)
if form.is_valid():
    print("Form is valid!")
else:
    print("Form Errors:")
    print(form.errors.as_data())
    for field, errors in form.errors.items():
        print(f"Field: {field}, Errors: {errors}")
