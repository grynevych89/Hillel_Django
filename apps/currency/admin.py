from django.contrib import admin
from currency.models import Rate, ContactUs


@admin.register(Rate)
class RateAdmin(admin.ModelAdmin):
    list_display_links = ('id', 'currency')
    list_display = ['id', 'currency', 'sell', 'buy', 'source', 'created']
    list_editable = ('sell', 'buy', 'source')
    list_filter = ['source']
    fieldsets = (
        ('Основне', {'fields': ('currency', 'sell', 'buy', 'source',), }),
    )


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display_links = ('id', 'subject')
    list_display = ['id', 'subject', 'email_from', 'message']
    list_editable = ('email_from',)
    list_filter = ['email_from']

    fieldsets = (
        ('Основне', {'fields': ('subject', 'email_from', 'message',), }),
    )

