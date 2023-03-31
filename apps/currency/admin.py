from django.contrib import admin
from rangefilter.filters import DateRangeFilter
from currency.models import Rate, RateSource


@admin.register(Rate)
class RateAdmin(admin.ModelAdmin):
    list_display_links = ('id',)
    list_display = ['id', 'currency', 'sale', 'buy', 'source', 'created']
    list_editable = ('sale', 'buy', 'source')
    list_filter = (
        'currency',
        ('created', DateRangeFilter)
    )
    search_fields = (
        'source',
        'buy',
        'sale',
    )


admin.site.register(RateSource)
