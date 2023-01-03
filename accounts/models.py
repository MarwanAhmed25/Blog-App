from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
import uuid
from django.urls import reverse
# Create your models here.

RATE = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
)


class CustomUser(AbstractUser):
    id = models.UUIDField(_("id"), default=uuid.uuid4, primary_key=True, editable=False)
    img = models.ImageField(_("image"), upload_to='profile_images/')
    updated_at = models.DateTimeField(_("updated_at"), auto_now=True, auto_now_add=False)
    birthday = models.DateTimeField(_("birthday"), auto_now=False, auto_now_add=False, null=True, blank=True)
    

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse("accounts", args=['str'(self.id)])
    

class Teacher(CustomUser):
    reviwed = models.IntegerField(_("reviewed"))

    def __str__(self):
        return self.username
    
    class Meta:
        managed = True
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'

class Review(models.Model):
    teacher = models.ForeignKey("Teacher", verbose_name=_("teacher"), related_name='reviewed',on_delete=models.CASCADE)
    rate = models.CharField(_("rate"), max_length=50, choices=RATE, null=False, blank=False)

    def save(self, *args, **kwargs):
        #if self.rate is not None:
         #   self.teacher_id
        super().save(self, *args, **kwargs)

    def __str__(self):
        return self.rate
    
    