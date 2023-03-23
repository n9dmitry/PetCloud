# Подключение для рендера
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
# Подключение стандартной формы для регистрации
from django.contrib.auth.forms import UserCreationForm


# Функция регистрации
# from petcloud.registr.forms import PostForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView

from .forms import *
from .models import Profile

class SignUp(CreateView):
    """Вьюха регистрации на сайте"""
    template_name = 'registr/register.html'
    form_class = SignUpForm
    success_url = reverse_lazy('news/news_form.html')


class ProfileView(DetailView):
    """Просмотр профиля"""
    model = Profile
    template_name = 'registr/profile_view.html'
    context_object_name = 'profileview'

class ProfileUpdateView(UpdateView):
    model = Profile
    form_class = ProfileChangeForm
    #fields = ('__all__')
    template_name = 'registr/profile_update.html'

    def get_success_url(self):
        return reverse_lazy('profile_view', kwargs ={'pk': self.object.pk})

    def get_queryset(self):
        return Profile.objects.filter(user = self.request.user)





