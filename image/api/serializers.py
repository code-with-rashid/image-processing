import base64

from rest_framework import serializers

from image.models import ImageModel


class BinaryImageField(serializers.ImageField):
    def to_representation(self, value):
        if value:
            try:
                # Open the image file
                with open(value.path, "rb") as img_file:
                    # Encode the binary image data in Base64
                    image_data_base64 = base64.b64encode(img_file.read())
                    return image_data_base64.decode("utf-8")  # Convert to UTF-8 for JSON serialization
            except Exception as e:
                # Handle any exceptions that may occur during image processing
                print(f"Error processing image: {e}")

        return None


class ImageReadSerializer(serializers.ModelSerializer):
    image = BinaryImageField()

    class Meta:
        model = ImageModel
        fields = (
            "id",
            "depth",
            "image",
        )
