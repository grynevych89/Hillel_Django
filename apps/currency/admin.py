from django.contrib import admin
from rangefilter.filters import DateRangeFilter
from currency.models import Rate, Source


@admin.register(Rate)
class RateAdmin(admin.ModelAdmin):
    list_display_links = ('id',)
    list_display = ['id', 'currency', 'sell', 'buy', 'source', 'created']
    list_editable = ('sell', 'buy', 'source')
    list_filter = (
        'currency',
        ('created', DateRangeFilter)
    )
    search_fields = (
        'source',
        'buy',
        'sell',
    )


admin.site.register(Source)
