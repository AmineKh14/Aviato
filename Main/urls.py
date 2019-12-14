from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login', views.login_request, name='login'),
    path('',views.index, name='home')
]
