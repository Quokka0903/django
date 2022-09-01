import random
from django.shortcuts import render

age = range(25, 31)
grade = ['a', 'b', 'c', 's']

# Create your views here.
def certification1(request):
    age_pick = random.choice(age)
    grade_pick = random.choice(grade)
    info = {
        'name' : 'A은성',
    }

    context = {
        'age_pick' : age_pick,
        'grade_pick' : grade_pick,
        'info' : info,
    }
    return render(request, 'certification1.html', context)

def certification2(request):
    age_pick = random.choice(age)
    grade_pick = random.choice(grade)
    info = {
        'name' : '박육찬',
    }

    context = {
        'age_pick' : age_pick,
        'grade_pick' : grade_pick,
        'info' : info,
    }
    return render(request, 'certification2.html', context)

def certification3(request):
    age_pick = random.choice(age)
    grade_pick = random.choice(grade)
    info = {
        'name' : '김빵준',
    }

    context = {
        'age_pick' : age_pick,
        'grade_pick' : grade_pick,
        'info' : info,
    }
    return render(request, 'certification2.html', context)