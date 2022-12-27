from django.urls import path

from . import views

app_name = 'library'

urlpatterns = [
    path('author/<int:pk>/', views.AuthorDetailView.as_view(), name='author'),
    path('author_list/', views.AuthorListView.as_view(), name='author_list'),
    path('book/<int:pk>/', views.BookDetailView.as_view(), name='book'),
    path('book_list/', views.BookListView.as_view(), name='book_list'),
    path('genre/<int:pk>/', views.GenreDetailView.as_view(), name='genre'),
    path('genre_list/', views.GenreListView.as_view(), name='genre_list'),
    path('reward/<int:pk>/', views.RewardDetailView.as_view(), name='reward'),
    path('reward_list/', views.RewardListView.as_view(), name='reward_list'),
    path('', views.main_view, name='main'),
]
