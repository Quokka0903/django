from django.shortcuts import render

# Create your views here.
def calculator(request, val1, val2):
    flag = 0
    if val2 == 0:
        flag = 1
    context = {
        'val1' : val1,
        'val2' : val2,
        'val2_min' : -val2,
        'flag' : flag,
    }

    return render(request, 'calculators/calculator.html', context)