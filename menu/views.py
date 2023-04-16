from django.shortcuts import render
from .models import Category


def index(request):
    left = 0
    right = 0
    return render(request, 'index.html', {
        "left": left,
        "right": right
    })


def menu_item(request, item):
    menu_item = Category.objects.get(title=item)
    left = menu_item.left
    right = menu_item.right
    return render(request, 'index.html', {
        "pointer": item,
        "left": left,
        "right": right
    })