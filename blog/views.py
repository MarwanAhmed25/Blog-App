from .forms import BlogForm, CommentForm
from django.views import generic
from .models import Blog

# Create your views here.

class BlogList(generic.ListView):
    model = Blog
    context_object_name = 'blog_list'
    template_name = 'list.html'


class BlogDetail(generic.DetailView):
    model = Blog
    context_object_name = 'blog'
    template_name = 'detail.html'
    

class BlogCreateView(generic.CreateView):
    model = Blog
    template_name = "create.html"
    form_class = BlogForm


class BlogUpdateView(generic.UpdateView):
    model = Blog
    template_name = "update.html"
    form_class = BlogForm


class BlogDeleteView(generic.DeleteView):
    model = Blog
    template_name = "delete.html"


