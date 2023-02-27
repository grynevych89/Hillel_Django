from django.contrib import admin
from source.models import Source


@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    list_display_links = ('name',)
    list_display = ['id', 'name', 'source_url', 'price']
    fieldsets = (
        ('Основне', {'fields': ('name', 'text', 'source_url', 'price',), }),
    )
