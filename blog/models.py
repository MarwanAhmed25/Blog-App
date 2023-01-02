from django.db import models
from accounts.models import CustomUser, Teacher
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
# Create your models here.

class Blog(models.Model):
    subject = models.CharField(_("subject"), max_length=250)
    title = models.CharField(_("title"), max_length=250, unique=True)
    body = models.TextField(_("body"))
    teacher = models.ForeignKey(Teacher, verbose_name=_("teacher"), on_delete=models.CASCADE)
    created_at = models.DateTimeField(_("created_at"), auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(_("updated_at"), auto_now=True, auto_now_add=False)
    slug = models.SlugField(_("slug"))

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        
        self.slug = slugify(self.title)
        super().save(self, *args, **kwargs)


class Comment(models.Model):
    body = models.TextField(_("body"))
    user = models.ForeignKey(CustomUser, verbose_name=_("teacher"), on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, verbose_name=_("blog"), on_delete=models.CASCADE)
    created_at = models.DateTimeField(_("created_at"), auto_now=True, auto_now_add=False)
    
    def __str__(self) -> str:
        return self.body



