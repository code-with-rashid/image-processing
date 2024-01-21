import os
import uuid

from django.conf import settings
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.contrib import messages
from django.core.management import call_command

from .forms import CSVImportForm


class CSVImportView(View):
    template_name = 'csv_import.html'
    form_class = CSVImportForm
    success_url = reverse_lazy("image:process_csv")

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)

        if form.is_valid():
            csv_file = form.cleaned_data['csv_file']
            file_path = self.handle_uploaded_file(csv_file)

            try:
                call_command('process_excel_images', file_path)
                messages.success(request, 'CSV file processed successfully')
                return redirect(self.success_url)
            except Exception as e:
                messages.error(request, f'An error occurred: {str(e)}')

        return render(request, self.template_name, {'form': form})

    @staticmethod
    def handle_uploaded_file(csv_file):
        target_directory = os.path.join(settings.MEDIA_ROOT, 'csv_files')

        # Create the target directory if it doesn't exist
        if not os.path.exists(target_directory):
            os.makedirs(target_directory)

        # Generate a unique filename using UUID
        unique_filename = f"{uuid.uuid4().hex}_{csv_file.name}"
        file_path = os.path.join(target_directory, unique_filename)

        with open(file_path, 'wb') as destination:
            for chunk in csv_file.chunks():
                destination.write(chunk)

        return file_path
