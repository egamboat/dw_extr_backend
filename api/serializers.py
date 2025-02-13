from rest_framework import serializers
from .models import CSVFile, BenchmarkReport


class CSVFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CSVFile
        fields = ['id', 'user','name','description', 'file', 'uploaded_at']
        read_only_fields = ['id','user', 'uploaded_at']

class BenchmarkReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = BenchmarkReport
        fields = ['id', 'user','name','description', 'benchmark_file', 'generated_at']
        read_only_fields = ['id', 'user', 'generated_at']