from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.BlogList.as_view(), name='list'),
    path('create/', views.BlogCreateView.as_view(), name='create'),
    path('update/<uuid:pk>/', views.BlogUpdateView.as_view(), name='update'),
    path('delete/<uuid:pk>/', views.BlogDeleteView.as_view(), name='delete'),
    path('<uuid:pk>/', views.BlogDetail.as_view(), name='detail'),
    
]
