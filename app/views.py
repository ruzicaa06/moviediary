from django.shortcuts import render, redirect
from .forms import MovieForm
from .models import Movie

def index(request):
    movies = Movie.objects.all()
    return render(request, 'index.html', context={'movies': movies})

def add_movie(request):
    if request.method == "POST":
        form_data = MovieForm(data=request.POST, files=request.FILES)
        if form_data.is_valid():
            movie = form_data.save(commit=False)
            movie.save()
            return redirect('/')
    return render(request, 'add_movie.html', {'form': MovieForm})

def edit_movie(request, pk):
    movie_instance = Movie.objects.filter(id=pk).get()
    if request.method == "POST":
        form_data = MovieForm(data=request.POST, files=request.FILES, instance=movie_instance)
        if form_data.is_valid():
            form_data.save()
        return redirect('/')
    else:
        movie = MovieForm(instance=movie_instance)
    return render(request, 'edit_movie.html', context={'form': movie})


def delete_movie(request, pk):
    movie_instance = Movie.objects.filter(id=pk).get()
    if request.method == "POST":
        movie_instance.delete()
        return redirect('/')
    return render(request, 'delete_movie.html')