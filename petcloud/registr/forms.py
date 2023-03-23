from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from .models import Profile

class SignUpForm(UserCreationForm):
    '''Форма регистрации юзера'''
    class Meta:
        model = Profile
        #fields = ('__all__')
        fields = ('username', 'avatar', 'email')

    # def save(self, commit=True):
    #     '''Создаем юзера и передаем данные. Создаем экземпляр профиля и передаем данные модели юзер'''
    #     user = super(UserCreationForm, self).save(commit=False)
    #     user.set_password(self.cleaned_data["password1"])
    #     user.username = (self.cleaned_data["username"])
    #     user.avatar = (self.cleaned_data["avatar"])
    #     if commit:
    #         user.save()
    #         profile = Profile(user = user, email = user.email)
    #         profile.save()
    #     return user

class ProfileChangeForm(UserChangeForm):
    """Форма профиля"""
    class Meta:
        model = Profile
        fields = ('username', 'email', 'avatar')
