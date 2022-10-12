from django.http import HttpResponse
from django.shortcuts import render

#METHOD VIEW INDEX / FUNCTIOn

def view1(request):
    return HttpResponse("<h1> Ini adalah view pertama </h1>")

def view2(request):
    return HttpResponse("<h2> Ini adalah view kedua </h2>")
