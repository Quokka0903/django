from django.shortcuts import render, redirect
from .models import Movie

# Create your views here.
def index(request):
    lists = Movie.objects.all()
    nerimcha = Movie.objects.order_by('-pk').all()
    context = {
        'lists' : lists,
        'nerimcha' : nerimcha,
    }
    return render(request, 'movies/index.html', context)

def new(request):
    genres = ["action", "crime", "SF", "Comedy", "romance", "thriller", "horror", "war", "sports", "fantasy", "music", "melo", "drama", "animation"]
    context = {
        'genres' : genres
    }
    return render(request, 'movies/new.html', context)

def create(request):
    title = request.GET.get('title')
    audience = request.GET.get('audience')
    release_date  = request.GET.get('release_date')
    genre = request.GET.get('genre')
    score = request.GET.get('score')
    poster_url = request.GET.get('poster_url')
    description = request.GET.get('description')

    film = Movie(title=title, audience=audience, release_date=release_date, genre=genre, score=score, poster_url=poster_url, description=description)
    film.save()
    return redirect('movies:detail', film.pk)

def detail(request, pk):
    film = Movie.objects.get(pk=pk)
    context = {
        'film': film,
    }
    return render(request, 'movies/detail.html', context)

def edit(request, pk):
    genres = ["action", "crime", "SF", "Comedy", "romance", "thriller", "horror", "war", "sports", "fantasy", "music", "melo", "drama", "animation"]
    film = Movie.objects.get(pk=pk)
    context = {
        'film': film,
        'genres' : genres
    }
    return render(request, 'movies/edit.html', context)

def update(request, pk):
    film = Movie.objects.get(pk=pk)
    film.title = request.POST.get('title')
    film.audience = request.POST.get('audience')
    film.release_date = request.POST.get('release_date')
    film.genre = request.POST.get('genre')
    film.score = request.POST.get('score')
    film.poster_url = request.POST.get('poster_url')
    film.description = request.POST.get('description')
    film.save()

    return redirect('movies:detail', film.pk)

def delete(request, pk):
    film = Movie.objects.get(pk=pk)
    film.delete()
    return redirect('movies:index')