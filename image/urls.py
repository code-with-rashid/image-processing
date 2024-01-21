from django.urls import path
from .views import CSVImportView

app_name = "image"

urlpatterns = [
    path('process-csv/', CSVImportView.as_view(), name='process_csv'),
]
