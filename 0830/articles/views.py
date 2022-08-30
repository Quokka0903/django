from email import message
from django.shortcuts import render
import random

# Create your views here.

def index(request):
    return render(request, 'index.html')


def greeting(request):
    foods = ['apple', 'banana', 'coconut',]
    info = {
        'name' : 'greg',
    }
    context = {
        'foods' : foods,
        'info' : info,
    }
    return render(request, 'greeting.html', context)

def dinner(request):
    foods = ['족발', '치킨', '라면', '초밥', '치즈피자', '에멘탈치즈샐러드', '엄마가해주신된장국']
    pick = random.choice(foods)
    context = {
        'pick' : pick,
        'foods' : foods,
    }
    return render(request, 'dinner.html', context)

def throw(request):
    return render(request, 'throw.html')

def catch(request):
    message = request.GET.get('message')
    context = {
        'message' : message,
    }
    return render(request, 'catch.html', context)

def hello(request, name):
    context = {
        'name' : name,
    }
    return render(request, 'hello.html', context)