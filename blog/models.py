from django.db import models
from accounts.models import CustomUser, Teacher
from django.utils.translation import gettext_lazy as _
import uuid
from django.urls import reverse
# Create your models here.

class Blog(models.Model):
    id = models.UUIDField(_("id"), editable=False, primary_key=True, default=uuid.uuid4)
    subject = models.CharField(_("subject"), max_length=250)
    title = models.CharField(_("title"), max_length=250, unique=True)
    body = models.TextField(_("body"))
    teacher = models.ForeignKey(Teacher, verbose_name=_("teacher"), on_delete=models.CASCADE)
    created_at = models.DateTimeField(_("created_at"), auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(_("updated_at"), auto_now=True, auto_now_add=False)
    

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse("blogs", args=["str"(self.id)])
    


class Comment(models.Model):
    body = models.TextField(_("body"))
    user = models.ForeignKey(CustomUser, verbose_name=_("teacher"), on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, verbose_name=_("blog"), related_name='comments',on_delete=models.CASCADE)
    created_at = models.DateTimeField(_("created_at"), auto_now=True, auto_now_add=False)
    
    def __str__(self) -> str:
        return self.body



