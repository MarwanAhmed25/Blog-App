from django.views.generic import ListView
from django.shortcuts import render
from accounts.models import Teacher
from blog.models import Blog

class HomeView(ListView):
    template_name = "_base.html"
    model = Teacher
    queryset = Teacher.objects.all().order_by('-reviwed')
    context_object_name = 'teacher_list'
    


home = HomeView.as_view()