from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from image.models import ImageModel
from image.factories import ImageModelFactory


class Tests(APITestCase):
    def setUp(self) -> None:
        super().setUp()

        self.images_count = 20
        for _ in range(self.images_count):
            ImageModelFactory()

    def test_list_images(self):
        self.assertEqual(ImageModel.objects.count(), self.images_count)

        response = self.client.get(
            reverse('image_api:image-list'),
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], self.images_count)

        newly_added_images_count = 5
        for _ in range(newly_added_images_count):
            ImageModelFactory()

        response = self.client.get(
            reverse('image_api:image-list'),
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], self.images_count + newly_added_images_count)

    def test_filter_by_depth_range_in_list_images(self):
        ImageModelFactory(depth=10000)
        ImageModelFactory(depth=10000.1)
        ImageModelFactory(depth=10000.2)
        ImageModelFactory(depth=10000.3)
        ImageModelFactory(depth=10000.8)

        response = self.client.get(
            f"{reverse('image_api:image-list')}?depth_max=10000.5&depth_min=10000",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'],
                         ImageModel.objects.filter(depth__gte=10000, depth__lte=10000.5).count())

        response = self.client.get(
            f"{reverse('image_api:image-list')}?depth_max=10000.9&depth_min=10000",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'],
                         ImageModel.objects.filter(depth__gte=10000, depth__lte=10000.9).count())
