from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'role', 'is_active', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        ('Rôle utilisateur', {'fields': ('role',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Rôle utilisateur', {'fields': ('role',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
