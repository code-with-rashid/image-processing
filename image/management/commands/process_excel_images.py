import io
import os
import csv
import numpy as np
from matplotlib import cm
from PIL import Image as PilImage
from django.core.files import File
from django.core.management.base import BaseCommand
from django.conf import settings
from image.models import ImageModel


class Command(BaseCommand):
    help = 'Import and process images from CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', help='Path to the CSV file')

    def handle(self, *args, **options):
        csv_file_path = options['csv_file']
        file_path = self.get_absolute_path(csv_file_path)

        if not file_path:
            self.stdout.write(self.style.ERROR("CSV file not found at both given and absolute paths"))
            return

        try:
            self.import_and_process_images(file_path)
            self.stdout.write(self.style.SUCCESS("Images imported and processed successfully"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"An error occurred: {str(e)}"))

    @staticmethod
    def get_absolute_path(file_path):
        if os.path.exists(file_path):
            return file_path

        absolute_path = os.path.join(settings.ROOT_DIR, file_path)
        return absolute_path if os.path.exists(absolute_path) else None

    def import_and_process_images(self, file_path, batch_size=500):
        instances = []

        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            header = next(reader)  # Skip the header

            for row in reader:
                try:
                    depth, pixel_values = self.process_row(row)
                except ValueError:
                    # Skip rows with non-integer values
                    continue

                image_array = np.array(pixel_values[:150], dtype=np.uint8)
                image_array = image_array.reshape(-1, 150)
                image_array = image_array[:, :150]

                image_array_color_mapped = self.apply_custom_colormap(image_array)

                image = PilImage.fromarray(image_array_color_mapped)
                image_io = self.create_image_io(image)

                image_file = File(image_io, name=f'{depth}.jpg')

                image_model = ImageModel(depth=depth, image=image_file)
                instances.append(image_model)

                if len(instances) >= batch_size:
                    ImageModel.objects.bulk_create(instances)
                    instances = []

        # Create any remaining instances after the loop
        if instances:
            ImageModel.objects.bulk_create(instances)

    @staticmethod
    def process_row(row):
        depth = row[0]
        pixel_values = [int(value) for value in row[1:]]
        return depth, pixel_values

    @staticmethod
    def create_image_io(image):
        image_io = io.BytesIO()
        image.save(image_io, format='JPEG')
        return image_io

    @staticmethod
    def apply_custom_colormap(image_array):
        # Normalize pixel values to range [0, 1] for colormap
        normalized_image_array = image_array / 255.0

        # Apply the 'nipy_spectral' colormap
        colormapped_image = cm.nipy_spectral(normalized_image_array)

        # Scale back to [0, 255] and convert to uint8
        colormapped_image_array = (colormapped_image[:, :, :3] * 255).astype(np.uint8)

        return colormapped_image_array