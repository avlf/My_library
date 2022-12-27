from django.views import generic
from django.shortcuts import render

from .models import Author, Book, Genre, Reward


class AuthorListView(generic.ListView):
    model = Author
    template_name = 'author/author_list.html'
    context_object_name = "author_list"


class AuthorDetailView(generic.DetailView):
    model = Author
    template_name = 'author/author.html'
    context_object_name = "author"


class BookListView(generic.ListView):
    model = Book
    template_name = 'book/book_list.html'
    context_object_name = "book_list"


class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'book/book.html'
    context_object_name = "book"


class GenreListView(generic.ListView):
    model = Genre
    template_name = 'genre/genre_list.html'
    context_object_name = "genre_list"


class GenreDetailView(generic.DetailView):
    model = Genre
    template_name = 'genre/genre.html'
    context_object_name = "genre"


class RewardListView(generic.ListView):
    model = Reward
    template_name = 'reward/reward_list.html'
    context_object_name = "reward_list"


class RewardDetailView(generic.DetailView):
    model = Reward
    template_name = 'reward/reward.html'
    context_object_name = "reward"

def main_view(request):
    return render(request, 'main.html')
