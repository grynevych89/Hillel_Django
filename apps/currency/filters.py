import django_filters

from currency.models import Rate


class RateFilter(django_filters.FilterSet):
    class Meta:
        model = Rate
        fields = ['buy', 'sale', 'source', 'currency']


class RateFilterApi(django_filters.FilterSet):
    class Meta:
        model = Rate
        fields = {
            'source': ('exact', ),
            'currency': ('exact', ),
            'buy': ('gt', 'gte', 'lt', 'lte', 'exact'),
            'sale': ('gt', 'gte', 'lt', 'lte', 'exact'),
        }
