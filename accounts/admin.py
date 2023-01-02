from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import Review, Teacher
# Register your models here.

CustomUser = get_user_model()

class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    model = CustomUser
    UserAdmin.fieldsets += (('New Fields', {'fields': ('img', 'birthday')}),)
    
    

admin.site.register(CustomUser, CustomUserAdmin)


class TeacherAdmin(admin.ModelAdmin):
    model = Teacher
    exclude = ('slug',)

admin.site.register(Review)
admin.site.register(Teacher, TeacherAdmin)