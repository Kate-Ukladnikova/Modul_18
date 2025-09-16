from django.http import HttpResponse
from django.shortcuts import render
from task5.forms import UserRegister

# Create your views here.

users = ['Kate', 'Andrey', 'George']
context = {'base_name': 'Домашнее задание по теме "Формы отправки данных. HTML и Django формы"',
           'base_aim': 'Цель: понять на практике как работают POST запросы в Django. '
                        'Использовать формы для обработки этих запросов.',
           'base_task': 'Задача "Имитация регистрации":',
           'base_time': '16.09.2025 г.',
           'base_student': 'Укладникова Екатерина Львовна'
           }

def sign_up_by_html(request):
    context['base_title'] = 'Регистрация - sign_up_by_html'
    if request.method == "POST":
        # Получаем данные:
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = int(request.POST.get('age'))

        print(f"Username: {username}")
        print(f"Password: {password}")
        print(f"repeat_password: {repeat_password}")
        print(f"Age: {age}")
        context["username"]=username
        context["password"] = password
        context["repeat_password"] = repeat_password
        context["age"] = age
        data_verification(username, password, repeat_password, age)

    # Если это GET или ошибка POST:
    return render(request, 'fifth_task/registration_page.html', context)

def sign_up_by_django(request):
    context['base_title'] = 'Регистрация - sign_up_by_django'
    if request.method == "POST":
        form = UserRegister(request.POST)
        if form.is_valid():
            # Обработка данных формы:
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            context["username"] = username
            context["password"] = password
            context["repeat_password"] = repeat_password
            context["age"] = age
            data_verification(username, password, repeat_password, age)

        context['form'] = form
    return render(request, 'fifth_task/registration_page.html', context)

def data_verification(username, password, repeat_password, age):
    if username in users:
        context['message'] = f'Пользователь {username} уже зарегистрирован в системе'
        print(f"Пользователь {username} уже зарегистрирован в системе")
    elif password != repeat_password:
        context['message'] = 'Данные пароли не совпадают'
        print("Пароли не совпадают.")
    elif len(str(age)) >= 4:
        context['message'] = 'Число символов возраста не должно превышать трёх символов и не равно нулю!'
        print(f"Число символов возраста {age} не должно превышать трёх и не может равняться нулю!")
    elif age <= 18:
        context['message'] = "Вы должны быть старше 18."
        print(f"Ваш возраст {age}, вы должны быть старше 18.")
    else:
        context['message'] = f'Приветствуем, {username}!'
        users.append(username)
        print(f"{username} добавлен в users")
    return(context, users)