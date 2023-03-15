from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display_links = ('id', 'username')
    list_display = ['id', 'username', 'email', 'is_staff', 'is_active', ]
    list_filter = ['email']
    readonly_fields = ['unique_id']
