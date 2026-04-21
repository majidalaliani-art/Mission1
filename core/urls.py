from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('report/', views.report_create_view, name='report_create'),
    path('success/', views.success_view, name='success'),
]
