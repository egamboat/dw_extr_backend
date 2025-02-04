
from django.contrib import admin
from django.contrib.auth.models import User
from .models import CustomUser, CSVFile

# Registrar el modelo User en el admin
admin.site.register(CustomUser)
admin.site.register(CSVFile)
