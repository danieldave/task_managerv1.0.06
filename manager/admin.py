from django.contrib import admin
from .models import Task, CustomUser

admin.site.register(Task)
admin.register(CustomUser)


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'name', 'phone_number', 'date_of_birth', 'office')  # Customize the fields to display in the list view
    search_fields = ('username', 'email', 'name', 'phone_number')  # Enable searching for these fields
    list_filter = ('office',)  # Add a filter by 'office' field
    ordering = ('-date_joined',)  # Sort users by date of registration (newest first)
    fieldsets = (
        ('Personal Information', {
            'fields': ('username', 'email', 'name', 'phone_number', 'date_of_birth', 'office', 'profile_picture', 'home_address')
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined'),
        }),
    )