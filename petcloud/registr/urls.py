from django.urls import path, include
from news.views import *
from registr.views import *
from oblako.views import *
from django.contrib.auth import views as auth_views
from registr.views import *



urlpatterns = [
path('<int:pk>/', ProfileView.as_view(), name='profile_view'),
path('profile_update/', ProfileUpdateView.as_view(), name='profile_update'),
path('registr/', SignUp.as_view(), name='signup'),
]