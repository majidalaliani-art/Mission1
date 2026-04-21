from django import forms
from .models import Report

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['region', 'site_type', 'location']
        widgets = {
            'region': forms.RadioSelect(),
            'site_type': forms.RadioSelect(),
            'location': forms.TextInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # جعل الحقول غير إلزامية في الاستمارة لأننا سنتعامل معها برمجياً أو عبر الراديو
        for field in self.fields:
            self.fields[field].required = False
