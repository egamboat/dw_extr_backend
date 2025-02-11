from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import CSVFileViewSet

router = DefaultRouter()
router.register(r'csv_files', CSVFileViewSet, basename='csvfile')

urlpatterns = [
    path('', include(router.urls)),
]
