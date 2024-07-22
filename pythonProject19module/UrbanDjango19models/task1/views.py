
from django.shortcuts import render, redirect
from .forms import UserRegister
from .models import *

def sign_up_by_django(request):
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            repeat_password = form.cleaned_data.get('repeat_password')
            age = form.cleaned_data.get('age')

            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
            elif Buyer.objects.filter(name=username).exists():
                info['error'] = 'Пользователь уже существует'
            else:
                # Добавление нового пользователя в базу данных
                Buyer.objects.create(name=username, balance=0.00, age=age)
                return redirect('platform/')

        info['form'] = form
    else:
        form = UserRegister()
        info['form'] = form

    return render(request, 'registration_page.html', info)

# def sign_up_by_html(request):
#     info = {}
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         repeat_password = request.POST.get('repeat_password')
#         try:
#             age = int(request.POST.get('age', 0))
#         except ValueError:
#             info['error'] = 'Некорректное значение возраста'
#
#         if 'error' not in info:
#             if password != repeat_password:
#                 info['error'] = 'Пароли не совпадают'
#             elif age < 18:
#                 info['error'] = 'Вы должны быть старше 18'
#             elif username in users:
#                 info['error'] = 'Пользователь уже существует'
#             else:
#                 info['message'] = f"Приветствуем, {username}!"
#                 users.append(username)
#
#     if request.method == 'GET':
#         info['username'] = ''
#         info['age'] = 0
#
#     return render(request, 'fifth_task/registration_page.html', info)



# from django.shortcuts import render
def index_platform(request):

    return render(request, 'platform.html', {"title": "ГЛАВНАЯ СТРАНИЦА"})
#
#
#
def index_magazine(request):
    games = Game.objects.all()  # Получаем все игры из базы данных
    return render(request, 'magazine.html', {"title": "ИГРЫ", "games": games})
#
def index_basket(request):

    return render(request, 'basket.html', {"title": "КОРЗИНА"})