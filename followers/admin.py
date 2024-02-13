from django.contrib import admin
from .models import Follower

# Register your models here.

@admin.register(Follower)
class FollowerAdmin(admin.ModelAdmin):
    list_display = ('creator', 'followed', 'created_at')
    search_fields = ('creator__username', 'followed__username')
    list_filter = ('created_at',)