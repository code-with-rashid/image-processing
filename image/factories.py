import factory
from io import BytesIO
from PIL import Image
from django.core.files import File
from .models import ImageModel


class ImageModelFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ImageModel

    depth = factory.Faker("pyfloat", positive=True)

    @classmethod
    def _generate(cls, create, attrs):
        # Create a synthetic grayscale image for testing in PNG format
        image = Image.new("L", (100, 100), "white")
        image_bytes_io = BytesIO()
        image.save(image_bytes_io, format="PNG")
        image_bytes_io.seek(0)

        attrs["image"] = File(image_bytes_io, name="test_image.png")

        return super()._generate(create, attrs)
