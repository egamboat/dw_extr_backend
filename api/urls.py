from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import CSVFileViewSet, BenchmarkReportViewSet

router = DefaultRouter()
router.register(r'csv_files', CSVFileViewSet, basename='csvfile')
router.register(r'benchmark-reports', BenchmarkReportViewSet, basename='benchmark')
urlpatterns = [
    path('', include(router.urls)),
]
