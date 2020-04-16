from django.contrib import admin
from .models import Post, Comment

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # Display the post list fields specified in the tuple.
    list_display = ('title', 'slug', 'author', 'publish', 'tags', 'status')
    # Filter results by the fields included in the tuple.
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')  # Specifies searchable fields
    # Input the slug field automatically by putting title.
    prepopulated_fields = {'slug': ('title', )}
    raw_id_fields = ('author', )
    date_hierarchy = "publish"  # Navigating through the date posted.
    ordering = ('status', 'publish')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')
