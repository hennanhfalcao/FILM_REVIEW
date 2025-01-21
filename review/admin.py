from django.contrib import admin
from .models import Review, Comment

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('title', 'slugify', 'status', 'published_at', 'author', 'rating')
    list_filter = ('status', 'author', 'rating')
    search_fields = ('title', 'body', 'author__username')
    prepopulated_fields = {'slugify': ('title',)}

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('review', 'user_name', 'user_email', 'message', 'active')
    list_filter = ('active', 'created_at')
    search_fields = ('user_name', 'user_email', 'message')