from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from .models import Chat
from .forms import ChatForm


# Create your views here.
@require_safe
def index(request):
    chattings = Chat.objects.all()
    context = {
        'chattings': chattings,
    }
    return render(request, 'chattings/index.html', context)


@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ChatForm(request.POST)
        if form.is_valid():
            Chat = form.save()
            return redirect('chattings:detail', Chat.pk)
    else:
        form = ChatForm()
    context = {
        'form': form,
    }
    return render(request, 'chattings/create.html', context)


@require_safe
def detail(request, pk):
    chat = Chat.objects.get(pk=pk)
    context = {
        'Chat': chat,
    }
    return render(request, 'chattings/detail.html', context)


@require_POST
def delete(request, pk):
    chat = Chat.objects.get(pk=pk)
    chat.delete()
    return redirect('chattings:index')

# @require_POST
# def delete(request, pk):
#     Chat = Chat.objects.get(pk=pk)
#     if request.user.is_authenticated:
#         if request.user == Chat.user:
#             Chat.delete()
#             return redirect('chattings:index')
#         return HttpResponseForbidden()
#     return HttpResponse(status=401)

@require_http_methods(['GET', 'POST'])
def update(request, pk):
    chat = Chat.objects.get(pk=pk)
    if request.method == 'POST':
        form = ChatForm(request.POST, instance=chat)
        if form.is_valid():
            form.save()
            return redirect('chattings:detail', chat.pk)
    else:
        form = ChatForm(instance=chat)

    context = {
        'form': form,
        'Chat': chat,
    }
    return render(request, 'chattings/update.html', context)
