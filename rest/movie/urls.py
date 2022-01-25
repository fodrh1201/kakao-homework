from django.contrib import admin
from django.urls import path, include
from movie import views

urlpatterns = [
    path('', views.movies, name="shop"),
    path('<int:id>', views.movie, name='menu'),
    # path('snippets/<int:pk>/', views.snippet_detail),
]