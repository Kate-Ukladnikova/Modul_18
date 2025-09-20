"""
URL configuration for UrbanDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
<<<<<<< HEAD
from django.urls import include, path
# from task2.views import func_template, ClassTemplate
# from task3.views import index, clothes, basket
<<<<<<< HEAD
# from task4.views import index, clothes, basket
from django.urls import path
from task5.views import sign_up_by_html, sign_up_by_django
=======
from task4.views import index, clothes, basket
=======
from django.urls import path
# from task2.views import func_template, ClassTemplate
# from task3.views import index, clothes, basket
# from task4.views import index, clothes, basket
from task5.views import sign_up_by_html, sign_up_by_django
>>>>>>> 2be7c96 (Добавлено выполненое задание task5.)
>>>>>>> 90c81fd2783d3f164f3f900168f4b06e73ae208d

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', index, name='index'),
    # path('', func_template), # Подключение маршрутов task2
    # path('class/', ClassTemplate.as_view()) # Метод as_view() подключает класс
    # path('platform/', index),  # Подключение маршрута task4: главная страница
    # path('clothes/', clothes),  # Подключение маршрута task4: женская одежда
    # path('basket/', basket),  # Подключение маршрута task4: корзина
    path('', sign_up_by_html), # Подключение маршрутов task5
    path('django_sign_up/', sign_up_by_django), # Подключение маршрутов task5
]
