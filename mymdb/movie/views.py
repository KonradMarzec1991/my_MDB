from django.views import generic
from django.shortcuts import render
from .models import Movie, Person


class MovieList(generic.ListView):
    model = Movie
    paginate_by = 10


class MovieDetail(generic.DetailView):
    model = Movie
    queryset = Movie.objects.all_with_related_persons()


class PersonDetail(generic.DetailView):
    model = Person
    queryset = Person.objects.all_with_prefetch_movies()