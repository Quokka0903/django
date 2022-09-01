from django.shortcuts import render


# Create your views here.
def first(request):
    message = request.GET.get('message')
    context = {
        'message' : message,
    }
    return render(request,'first.html', context)


def second(request):
    message = request.GET.get('message')
    context = {
        'message' : message,
    }
    return render(request,'second.html', context)


def third(request):
    message = request.GET.get('message')
    message2 = request.GET.get('message2')
    ran_list = [message, message2]
    context = {
        'ran_list' : ran_list,
        'message' : message,
        'message2' : message2,
    }
    return render(request,'third.html', context)