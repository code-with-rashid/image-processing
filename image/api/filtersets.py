from django.db.models import Q

from django_filters import rest_framework as filters

from image.models import ImageModel


class PolicyFilter(filters.FilterSet):
    depth = filters.RangeFilter()

    class Meta:
        model = ImageModel
        fields = (
            'depth',
        )
