from django.contrib import admin
from .models import Blog, Category

# Register your models here.

admin.site.register(Category)

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'status', 'is_featured', 'created_at')
    list_filter = ('status', 'is_featured', 'created_at')
    search_fields = ('title', 'category__name', 'status')
    list_editable = ('status', 'is_featured')
    prepopulated_fields = {'slug': ('title',)}
    
admin.site.register(Blog, BlogAdmin)
