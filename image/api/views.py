from django_filters import rest_framework as d_filters
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from . import serializers, filtersets
from ..models import ImageModel


class ImageListAPIView(ListAPIView):
    permission_classes = (AllowAny,)
    queryset = ImageModel.objects.all()
    serializer_class = serializers.ImageReadSerializer
    filter_backends = (d_filters.DjangoFilterBackend,)
    filterset_class = filtersets.PolicyFilter
