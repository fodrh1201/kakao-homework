from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http  import HttpResponse, JsonResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from movie.serializers import MovieSerializer
from django.utils import timezone
from pprint import pprint
import requests

def make_static_img_src(id):
    text = "{%static 'movie/images/" + str(id) + ".jpg' %}"
    return text
    
def movie(request):
    if request.method == 'GET':
        response = requests.get('http://127.0.0.1:8000/movie/')
        data = response.json()
        return render(request, 'movie/index.html', {'movie_list': data})

def about(request):
    if request.method == 'GET':
        return render(request, 'movie/about.html')
            
def upload(request):
    if request.method == 'GET':
        return render(request, 'movie/upload.html')

def detail(request, id):
    if request.method == 'GET':
        response = requests.get('http://127.0.0.1:8000/movie/' + str(id))
        data = response.json()
        return render(request, 'movie/detail.html', {'movie': data})