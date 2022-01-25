
from django.contrib import admin
from django.urls import path, include
from movie import views

urlpatterns = [
    path('', views.movie, name='movies'),
    path('about/', views.about, name='about'),
    path('upload/', views.upload, name='upload'),
    path('<int:id>', views.detail, name='detail')
]