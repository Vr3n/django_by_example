from django.contrib import admin
from .models import Post

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status') # Display the post list fields specified in the tuple.
    list_filter = ('status', 'created', 'publish', 'author') # Filter results by the fields included in the tuple.
    search_fields = ('title', 'body') # Specifies searchable fields
    prepopulated_fields = { 'slug': ('title', ) } # Input the slug field automatically by putting title.
    raw_id_fields = ('author', ) 
    date_hierarchy = "publish" # Navigating through the date posted.
    ordering = ('status', 'publish')
