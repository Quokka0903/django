from django.shortcuts import render
# Create your views here.
def price(request, name, val):
    product_price = {"라면":980,"홈런볼":1500,"칙촉":2300, "식빵":1800}
    if name in product_price:
        result = product_price[name] * val
    else:
        result = 0
    context = {
        'result' : result,
        'name' : name,
        'val' : val,
    }
    return render(request, 'price.html', context)