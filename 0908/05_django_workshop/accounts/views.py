from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from .models import User

# Create your views here.
def login(request):
    if request.method == 'POST':
        pass
    else:
        form = AuthenticationForm()
    contest = {
        'form' : form
    }
    return render(request, 'accounts/login.html', context)



def logout(request):
    pass



def signin(request):
    pass