from django.urls import path
from .views import CustomUserCreateView, CustomUserUpdateView, TeacherListView, TeacherDetailView, CustomUserDeleteView
app_name='accounts'

urlpatterns = [
    path('', TeacherListView.as_view(), name='list'),
    #path('update/<str:slug>/', CustomUserUpdateView.as_view(), name='update'),
    #path('signup/', CustomUserCreateView.as_view(), name='signup'),
    #path('delete/<str:slug>/', CustomUserDeleteView.as_view(), name='delete'),
    path('<uuid:pk>/', TeacherDetailView.as_view(), name='detail'),

]

