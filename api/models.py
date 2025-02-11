import os
from django.db import models
from django.conf import settings


# Modelo para Archivos CSV
def user_directory_path(instance, filename):
    return f'csv_files/user_{instance.user.id}/{filename}'


class CSVFile(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True, verbose_name="Nombre del archivo")
    description = models.TextField(null=True, blank=True, verbose_name="Descripción del archivo")

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    file = models.FileField(upload_to=user_directory_path)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name


# Modelo para Informes de Benchmark (solo CSV generado)
def benchmark_directory_path(instance, filename):
    return f'benchmarks/user_{instance.user.id}/{filename}'


class BenchmarkReport(models.Model):
    """Modelo que almacena los informes de benchmarks en formato CSV."""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    benchmark_file = models.FileField(upload_to=benchmark_directory_path)
    generated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Benchmark Report - {self.user.username} - {self.generated_at.strftime('%Y-%m-%d %H:%M')}"
