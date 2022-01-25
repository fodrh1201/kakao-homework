from django import views
from django.shortcuts import redirect, render

# Create your views here.
from django.http  import HttpResponse, JsonResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from movie.serializers import MovieSerializer
from django.utils import timezone
from pprint import pprint
import requests
import os

# host = 'rest'
rest_host = os.environ.get('REST_HOST', '127.0.0.1:8000')

def make_static_img_src(id):
    text = "{%static 'movie/images/" + str(id) + ".jpg' %}"
    return text
    
def movie(request):
    if request.method == 'GET':
        response = requests.get(f'http://{rest_host}/movie/')
        data = response.json()
        return render(request, 'movie/index.html', {'movie_list': data})

def about(request):
    if request.method == 'GET':
        return render(request, 'movie/about.html')
            
def upload(request):
    if request.method == 'GET':
        return render(request, 'movie/upload.html')
    elif request.method == 'POST':
        response = request.post(f'http://{rest_host}/movie/')
        data = response.json()
        return redirect(movie)

def detail(request, id):
    if request.method == 'GET':
        response = requests.get(f'http://{rest_host}/movie/' + str(id))
        data = response.json()
        return render(request, 'movie/detail.html', {'movie': data})