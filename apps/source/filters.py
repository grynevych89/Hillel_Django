import django_filters

from source.models import Source


class SourceFilter(django_filters.FilterSet):

    class Meta:
        model = Source
        fields = ['name', 'source_url', 'price']
