from django.shortcuts import render

# Create your views here.

def index(request):
    title = 'Интернет-магазин женской одежды "Катюша"'
    text = 'Главная страница'
    text2 = 'Женская одежда'
    text3 = 'Извините, ваша корзина пуста'
    context = {
        'title': title,
        'text': text,
        'text2': text2,
        'text3': text3,
    }
    return render(request, 'third_task/index.html', context)

def clothes(request):
    text2 = 'Женская одежда'
    context = {
        'text2': text2,
    }
    return render(request, 'third_task/clothes.html', context)

def basket(request):
    text3 = 'Извините, ваша корзина пуста'
    text4 = 'Корзина'
    context = {
        'text3': text3,
        'text4': text4,
    }
    return render(request, 'third_task/basket.html', context)