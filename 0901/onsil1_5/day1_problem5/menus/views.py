from django.shortcuts import render

drinks = ["cider", "coke", "miranda", "fanta", "eye of finetree"]
foods = ["피자", "치킨", "국밥", "초밥", "민초흑당로제마라탕"]

# Create your views here.
def food(request):
    context = {
        'food' : foods,
    }
    return render(request, 'food.html', context)


def drink(request):
    context = {
        'drink' : drinks,
    }
    return render(request, 'drink.html', context)


def receipt(request):
    message = request.GET.get('message').lower()
    if message not in foods and message not in drinks:
        flag = 0
    else:
        flag = 1

    context = {
        'message' : message,
        'flag' : flag,
    }
    return render(request, 'receipt.html', context)