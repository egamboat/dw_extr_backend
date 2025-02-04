from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .models import CSVFile
from .serializers import CSVFileSerializer

# Vista para listar y subir archivos CSV
@api_view(['GET', 'POST'])
def csv_file_list(request):
    if request.method == 'GET':
        csv_files = CSVFile.objects.filter(user=request.user)
        serializer = CSVFileSerializer(csv_files, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = CSVFileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
