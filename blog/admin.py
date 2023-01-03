from django.contrib import admin
from .models import Blog, Comment
# Register your models here.


class CommentAdmin(admin.TabularInline):
    model = Comment


class BlogAdmin(admin.ModelAdmin):
    inlines = [ CommentAdmin ]
    model = Blog
    exclude = ('slug',)

admin.site.register(Blog, BlogAdmin)
