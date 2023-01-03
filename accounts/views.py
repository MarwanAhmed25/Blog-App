from django.urls import reverse_lazy, reverse
from django.views import generic
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import Teacher
# Create your views here.


class CustomUserCreateView(generic.CreateView):

    model = get_user_model()
    form_class = CustomUserCreationForm
    template_name = 'signup.html'

    def get_success_url(self):
        return reverse('accounts:update',args=(self.object.slug,))



class CustomUserUpdateView(generic.UpdateView):
    model = get_user_model()
    form_class = CustomUserChangeForm
    success_url = reverse_lazy('home')
    template_name = 'update.html'

def t():
    print('nnnnnnnnnnnnnnnnnnnnnnnnnnn')

#CustomUserList, CustomUserDetail, CustomUserDelete
class TeacherListView(generic.ListView):
    
    model = Teacher
    context_object_name = 'teacher_list'
    template_name = "teacher_list.html"


class TeacherDetailView(generic.DetailView):
    model = Teacher
    context_object_name = 'teacher'
    template_name = "teacher_detail.html"


class CustomUserDeleteView(generic.DeleteView):
    model = get_user_model()
    success_url = reverse_lazy('home')
    template_name = "delete.html"
