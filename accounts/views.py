from django.urls import reverse_lazy, reverse
from django.views import generic
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm, CustomUserChangeForm
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


#CustomUserList, CustomUserDetail, CustomUserDelete
class CustomUserListView(generic.ListView):
    model = get_user_model()
    template_name = "list.html"


class CustomUserDetailView(generic.DetailView):
    model = get_user_model()
    template_name = "detail.html"


class CustomUserDeleteView(generic.DeleteView):
    model = get_user_model()
    success_url = reverse_lazy('home')
    template_name = "delete.html"
