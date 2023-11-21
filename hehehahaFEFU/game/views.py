from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import UserRegisterForm
from django.contrib import messages


def main_page(request):
    return redirect('login')


def user_reg(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрировались')
            return redirect('login')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()

    return render(request, 'game/register.html', {"form": form})


def user_log(request):
    return render(request, 'game/login.html')
