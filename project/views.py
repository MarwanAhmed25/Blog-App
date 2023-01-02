from django.views.generic import TemplateView
from django.shortcuts import render
from accounts.models import Teacher
from blog.models import Blog

class HomeView(TemplateView):
    template_name = "base_generic.html"


def home(request):
    teachers = Teacher.objects.all().order_by('reviwed')[:5]
    #print('t..', teachers)
    blogs = []

    for t in teachers:
        blogs.append(Blog.objects.get(teacher = t))

    

    return render(request, '_base.html', {'teachers': teachers, 'blogs':blogs})
