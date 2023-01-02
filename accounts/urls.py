from django.urls import path
from .views import CustomUserCreateView, CustomUserUpdateView, CustomUserListView, CustomUserDetailView, CustomUserDeleteView
app_name='accounts'

urlpatterns = [
    path('', CustomUserListView.as_view(), name='list'),
    path('update/<str:slug>/', CustomUserUpdateView.as_view(), name='update'),
    path('signup/', CustomUserCreateView.as_view(), name='signup'),
    path('delete/<str:slug>/', CustomUserDeleteView.as_view(), name='delete'),
    path('<str:slug>/', CustomUserDetailView.as_view(), name='detail'),

]

