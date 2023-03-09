from django.contrib import admin
from contacts.models import ContactUs, RequestResponseLog


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display_links = ('id', 'subject')
    list_display = ['id', 'name', 'subject', 'email_from', 'message', 'created', ]
    list_editable = ('email_from',)
    list_filter = ['email_from']

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(RequestResponseLog)
class RequestResponseLogAdmin(admin.ModelAdmin):
    list_display = ['id', 'path', 'request_method', 'time', ]
