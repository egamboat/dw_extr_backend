from django.urls import path
from . import views

urlpatterns = [
    path('csv_files/', views.csv_file_list, name='csv_file_list'),
]
