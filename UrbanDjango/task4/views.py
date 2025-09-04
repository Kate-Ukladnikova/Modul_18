from django.shortcuts import render

menu_ = {'Главная': ["http://127.0.0.1:8000/"], 'Магазин': ["http://127.0.0.1:8000/clothes/"],
         'Корзина': ["http://127.0.0.1:8000/basket/"]}


# Create your views here.
def get_menu(request):
    pagename = 'Главная страница'
    context = {
        'pagename': pagename,
        'menu': menu_,
    }
    return render(request, 'fourth_task/menu.html', context)

def index(request):
    pagename = 'Главная страница'
    title = 'Интернет-магазин "Катюша"'
    context = {
        'pagename': pagename,
        'title': title,
    }
    return render(request, 'fourth_task/index.html', context)

def clothes(request):
    pagename = 'Женская одежда'
    content = {'clothes': ["Головные уборы", "Платья", "Обувь"]}
    context = {
        'pagename': pagename,
        'content': content
    }
    return render(request, 'fourth_task/clothes.html', context)

def basket(request):
    pagename = 'Корзина'
    content = 'Извините, ваша корзина пуста'
    context = {
        'pagename': pagename,
        'content': content,
    }
    return render(request, 'fourth_task/basket.html', context)
