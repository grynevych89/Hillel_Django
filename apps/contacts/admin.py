from django.contrib import admin
from contacts.models import ContactUs


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display_links = ('id', 'subject')
    list_display = ['id', 'subject', 'email_from', 'message']
    list_editable = ('email_from',)
    list_filter = ['email_from']

    fieldsets = (
        ('Основне', {'fields': ('subject', 'email_from', 'message',), }),
    )
