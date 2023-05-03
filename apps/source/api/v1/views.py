from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.renderers import JSONRenderer
from rest_framework_xml.renderers import XMLRenderer
from rest_framework_yaml.renderers import YAMLRenderer
from rest_framework import filters as rest_framework_filters

from django_filters import rest_framework as filters

from source.api.v1.serializers import SourceSerializer
from source.filters import SourceFilterApi
from source.models import Source
from source.paginators import SourcePagination
# from source.throttlers import AnonSourceThrottle


class SourceViewSet(viewsets.ModelViewSet):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer
    renderer_classes = (JSONRenderer, XMLRenderer, YAMLRenderer)
    pagination_class = SourcePagination
    permission_classes = (AllowAny,)
    filter_backends = (
        filters.DjangoFilterBackend,
        rest_framework_filters.OrderingFilter,
    )
    filterset_class = SourceFilterApi
    ordering_fields = ('id', 'name', 'price', 'source_url')
    # throttle_classes = (AnonSourceThrottle,)
