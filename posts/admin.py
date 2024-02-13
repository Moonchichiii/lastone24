from django.contrib import admin
from .models import Post

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'creator', 'created_at', 'published')
    search_fields = ('title', 'creator__username')
    list_filter = ('created_at', 'published')
    actions = ['publish_posts', 'unpublish_posts']

    def publish_posts(self, request, queryset):
        queryset.update(published=True)
    publish_posts.short_description = "Publish selected posts"

    def unpublish_posts(self, request, queryset):
        queryset.update(published=False)
    unpublish_posts.short_description = "Unpublish selected posts"