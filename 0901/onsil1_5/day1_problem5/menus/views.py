from datetime import datetime
from django.shortcuts import render

drinks = ["cider", "coke", "miranda", "fanta", "eye of finetree"]
foods = ["피자", "치킨", "국밥", "초밥", "민초흑당로제마라탕"]

# Create your views here.
def food(request):
    context = {
        'food' : foods,
        'dongjun' : '1',
    }
    return render(request, 'food.html', context)


def drink(request):
    context = {
        'drink' : drinks,
        'dongjun' : '0',
    }
    return render(request, 'drink.html', context)


def receipt(request):
    message = request.GET.get('message').lower()
    dongjun = request.GET.get('dongjun')

    if message not in foods:
        res = '0'
    if message not in drinks:
        res = '1'
    
    print('res')
    print(res)
    context = {
        'message' : message,
        'dongjun' : dongjun,
        'res' : res,
    }
    return render(request, 'receipt.html', context)