from django.urls import path, include
from rest_framework import routers

from . import views

app_name = "image_api"


urlpatterns = [
    path(
        "images/",
        views.ImageListAPIView.as_view(),
        name="image-list",
    ),
]
