# Подключение для рендера
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
# Подключение стандартной формы для регистрации
from django.contrib.auth.forms import UserCreationForm


# Функция регистрации
from petcloud.registr.forms import PostForm
from petcloud.registr.models import Profile


def registr(request):
    # Массив для передачи данных шаблонны
    data = {}
    # Проверка что есть запрос POST
    if request.method == 'POST':
        # Создаём форму
        form = UserCreationForm(request.POST)
        # Валидация данных из формы
        if form.is_valid():
            # Сохраняем пользователя
            form.save()
            # Передача формы к рендару
            data['form'] = form
            # Передача надписи, если прошло всё успешно
            data['res'] = "Всё прошло успешно"
            # Рендаринг страницы
            return render(request, 'registr/registr.html', data)
    else:  # Иначе
        # Создаём форму
        form = UserCreationForm()
        # Передаём форму для рендеринга
        data['form'] = form
        # Рендаринг страницы
        return render(request, 'registr/registr.html', data)

@login_required
def editprofile(request):
    if request.method == 'POST':
        profile = Profile.objects.get(id=request.user.id)
        try:
            profile.username = request.POST['username']
        except:
            pass
        try:
            profile.email = request.POST['email']
        except:
            pass
        profile.save()
        return redirect('editprofile')




