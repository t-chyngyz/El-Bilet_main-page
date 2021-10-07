from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .forms import LoginForm

urlpatterns = [
    path ('login2/', views.user_login, name='login2'),
    path('login/', views.UserAuth.as_view(), name='login'),
    # path('login3/', auth_views.login, name='login3', kwargs={"authentication_form":LoginForm}),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path ('register/', views.register, name='register'),
]
