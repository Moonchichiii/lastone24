from django.contrib import admin
from .models import Profile

# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('creator', 'created_at', 'updated_at')
    search_fields = ('creator__username', 'name')
    list_filter = ('created_at', 'updated_at')