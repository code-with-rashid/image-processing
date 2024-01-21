from django import forms
from django.core.validators import FileExtensionValidator


class CSVImportForm(forms.Form):
    csv_file = forms.FileField(
        label='CSV File',
        validators=[FileExtensionValidator(allowed_extensions=['csv'])]
    )
