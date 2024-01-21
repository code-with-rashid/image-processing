from django.db import models


class ImageModel(models.Model):
    depth = models.DecimalField(max_digits=11, decimal_places=3, db_index=True)
    image = models.ImageField(upload_to="images",)

    def __str__(self):
        return f'{self.depth}'
