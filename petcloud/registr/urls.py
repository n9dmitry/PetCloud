from django.urls import path, include
from news.views import *
from registr.views import *
from oblako.views import *
from django.contrib.auth import views as auth_views
from registr.views import SignUp



urlpatterns = [
path('<int:pk>/', ProfileView.as_view(), name='profile_view'),
path('login/', auth_views.LoginView.as_view(template_name='registr/login.html')),
path('logout/', auth_views.LogoutView.as_view(template_name='registr/logout.html')),
path('profile_update/<int:pk>/', ProfileUpdateView.as_view(), name='profile_update'),
path('registr/', SignUp.as_view(), name='signup')
]