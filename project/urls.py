from django.contrib import admin
from django.urls import path, include
from .views import HomeView

urlpatterns = [
    path("admin/", admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('blogs/', include('blog.urls', namespace='blog')),
    path('', HomeView.as_view(), name='home'),
]
