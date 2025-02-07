
from django.contrib import admin
from django.contrib.auth.models import User
from .models import CSVFile

# Registrar el modelo User en el admin
admin.site.register(CSVFile)
