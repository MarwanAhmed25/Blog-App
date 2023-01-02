from django.contrib import admin
from .models import Blog, Comment
# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    model = Blog
    exclude = ('slug',)

admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment)
