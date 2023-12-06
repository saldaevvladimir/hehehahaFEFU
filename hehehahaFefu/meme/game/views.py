from django.shortcuts import render, redirect

from .forms import UserRegisterForm, UserLoginForm
from .models import Userdata
from django.contrib import messages
from django.contrib.auth import login, logout


def main_page(request):
    return redirect('login')


def user_reg(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            user_data = Userdata.objects.create(user=user)
            user_data.save()
            messages.success(request, 'Вы успешно зарегистрировались')
            return redirect('home')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()

    return render(request, 'game/register.html', {"form": form})


def user_log(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'game/login.html', {"form": form})


def user_logout(request):
    logout(request)
    return redirect('login')


def user_home(request):
    if request.user.is_authenticated:
        return render(request, 'game/home.html')
    else:
        return redirect('login')
