from django.views import generic
from django.shortcuts import render
from .models import Movie


class MovieList(generic.ListView):
    model = Movie
    paginate_by = 10


class MovieDetail(generic.DetailView):
    model = Movie