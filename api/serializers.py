from rest_framework import serializers
from .models import CSVFile

class CSVFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CSVFile
        fields = ['id', 'user','name','description', 'file', 'uploaded_at']
        read_only_fields = ['id','user', 'uploaded_at']
