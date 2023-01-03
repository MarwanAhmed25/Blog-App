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

################## Teachers #########################

class ReviewAdmin(admin.TabularInline):
    model = Review

class TeacherAdmin(admin.ModelAdmin):
    inlines = [ ReviewAdmin ]
    model = Teacher
    exclude = ('slug',)


admin.site.register(Teacher, TeacherAdmin)