from django.urls import path
from . import views

app_name = 'auths'

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.loginpage, name='login'),
    path('logout', views.logoutuser, name='logout'),
    path('register', views.register, name='register')
]