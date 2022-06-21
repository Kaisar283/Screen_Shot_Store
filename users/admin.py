from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import NewUser


class UserAdminConfig(UserAdmin):
    search_fields = ('email', 'user_name',)
    list_filter = ('email', 'user_name', 'is_staff', 'is_active',)
    ordering = ('-start_data',)
    list_display = ('email', 'user_name', 'is_active', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'user_name',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'user_name', 'password1', 'password2', 'is_active', 'is_staff')}
         ),
    )

admin.site.register(NewUser, UserAdminConfig)
