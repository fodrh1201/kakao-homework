from django.shortcuts import render, redirect
from pytz import timezone
from movie.models import Movie
from movie.serializers import MovieSerializer
from django.http  import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.utils import timezone
from pprint import pprint
import os

ui_host = os.environ.get('UI_HOST', '127.0.0.1:8001')

@csrf_exempt
def movies(request):
    if request.method == 'GET':
        # shops = Shop.objects.all()
        # serializer = ShopSerializer(shops, many=True)
        # return JsonResponse(serializer.data, safe=False)
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        movie = Movie(name=name, description=description)
        movie.save()
        return HttpResponse(status=200)


# Create your views here.
@csrf_exempt
def movie(request, id):
    if request.method == 'GET':
        movie = Movie.objects.get(pk=id)
        serializer = MovieSerializer(movie)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'DELETE':
        movie = Movie.objects.get(pk=id)
        movie.delete()
        return HttpResponse(status=200)
        
        
        
    # elif request.method == 'POST':
    #     data = JSONParser().parse(request)
    #     serializer = MenuSerializer(data=data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return JsonResponse(serializer.data, status=201)
    #     return JsonResponse(serializer.errors, status=400)