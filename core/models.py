from django.db import models
from django.contrib.auth.models import User

# نموذج الاستمارة (التقرير)
class Report(models.Model):
    REGION_CHOICES = [
        ('الملز', 'الملز'),
        ('العليا', 'العليا'),
        ('المعذر', 'المعذر'),
        ('البطحاء', 'البطحاء'),
        ('الشميسي', 'الشميسي'),
    ]

    SITE_TYPE_CHOICES = [
        ('مواقع', 'مواقع'),
        ('دورات مياه', 'دورات مياه'),
        ('مساحات انتشارية', 'مساحات انتشارية'),
    ]

    EVALUATION_CHOICES = [
        ('غير مطابق (غير موجود)', 'غير مطابق (غير موجود)'),
        ('غير منفذ', 'غير منفذ'),
        ('منفذ (100% إنجاز)', 'منفذ (100% إنجاز)'),
        ('منفذ ويوجد به ملاحظات جودة', 'منفذ ويوجد به ملاحظات جودة'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="القائم بالزيارة")
    region = models.CharField(max_length=100, choices=REGION_CHOICES, verbose_name="الوحدة")
    site_type = models.CharField(max_length=100, choices=SITE_TYPE_CHOICES, null=True, blank=True, verbose_name="نوع الموقع")
    location = models.CharField(max_length=500, null=True, blank=True, verbose_name="الموقع")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإنشاء")

    class Meta:
        verbose_name = "تقرير"
        verbose_name_plural = "التقارير"

    def __str__(self):
        return f"تقرير {self.region} - {self.created_at.strftime('%Y-%m-%d')}"

class ReportItemEvaluation(models.Model):
    report = models.ForeignKey(Report, on_delete=models.CASCADE, related_name='items', verbose_name="التقرير")
    item_name = models.CharField(max_length=500, verbose_name="اسم البند الفني")
    status = models.CharField(max_length=255, verbose_name="الحالة")

    class Meta:
        verbose_name = "سجل التقارير التفصيلي"
        verbose_name_plural = "سجل التقارير التفصيلي (جدول مدمج)"

    def __str__(self):
        return f"{self.item_name}: {self.status}"
class Location(models.Model):
    REGION_CHOICES = [
        ('الملز', 'الملز'),
        ('العليا', 'العليا'),
        ('المعذر', 'المعذر'),
        ('البطحاء', 'البطحاء'),
        ('الشميسي', 'الشميسي'),
    ]

    SITE_TYPE_CHOICES = [
        ('مواقع', 'مواقع'),
        ('دورات مياه', 'دورات مياه'),
        ('مساحات انتشارية', 'مساحات انتشارية'),
    ]

    name = models.CharField(max_length=500, verbose_name="اسم الموقع")
    region = models.CharField(max_length=100, choices=REGION_CHOICES, verbose_name="الوحدة")
    site_type = models.CharField(max_length=100, choices=SITE_TYPE_CHOICES, verbose_name="نوع الموقع")

    class Meta:
        verbose_name = "موقع"
        verbose_name_plural = "المواقع"
        unique_together = ('name', 'region', 'site_type')

    def __str__(self):
        return f"{self.name} ({self.region} - {self.site_type})"
