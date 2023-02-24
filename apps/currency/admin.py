from django.contrib import admin
from currency.models import Rate


@admin.register(Rate)
class RateAdmin(admin.ModelAdmin):
    list_display_links = ('id', 'currency')
    list_display = ['id', 'currency', 'sell', 'buy', 'source', 'created']
    list_editable = ('sell', 'buy', 'source')
    list_filter = ['source']
    fieldsets = (
        ('Основне', {'fields': ('currency', 'sell', 'buy', 'source',), }),
    )
