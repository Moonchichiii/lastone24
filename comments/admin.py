from django.contrib import admin
from .models import Comment

# Register your models here.

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('creator', 'post', 'created_at', 'content')
    search_fields = ('creator__username', 'post__title', 'content')
    list_filter = ('created_at', 'post')