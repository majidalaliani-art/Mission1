from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import LocationViewSet, ReportViewSet
from rest_framework.authtoken import views as auth_views

router = DefaultRouter()
router.register(r'locations', LocationViewSet)
router.register(r'reports', ReportViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', auth_views.obtain_auth_token),
]
