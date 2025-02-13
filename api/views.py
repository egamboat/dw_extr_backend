from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from .models import CSVFile, BenchmarkReport
from .serializers import CSVFileSerializer, BenchmarkReportSerializer

class CSVFileViewSet(ModelViewSet):
    serializer_class = CSVFileSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def get_queryset(self):
        return CSVFile.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class BenchmarkReportViewSet(ModelViewSet):
    serializer_class = BenchmarkReportSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]  # Permitir subida de archivos

    def get_queryset(self):
        return BenchmarkReport.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)