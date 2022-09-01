from django.shortcuts import render

# Create your views here.
def calculation(request):
    return render(request, 'calculation.html')

def result(request):
    first = request.GET.get('first')
    second = request.GET.get('second')

    context = {
        'first' : first,
        'second' : second,
        'min_second' : -1 * int(second),
    }

    if second != "0":
        context['nanum'] = int(first) / int(second)

    return render(request, 'result.html', context)