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

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
