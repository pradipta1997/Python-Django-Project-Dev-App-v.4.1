from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.

def index(request): #<--request itu sudah otomatis langsung membaca folder templates, yang mana sebelumnya sudah ter set di settings.py 

    #QuerySet
    posts = Post.objects.all() #<-- Query untuk mengambil semua data yang ada pada models class.
    print(posts)    #<-- Debug untuk memastikan QuerySet yang dapat dilihat di terminal / Checker.

    context = { # <--Template Variable
        'title':'Project Gallery',
        'contributor':'Pradipta Ramadhan',
        'directory':'templates/projectgallery/index.html',
        'posts':posts,
        'nav':[ # <--Template Tags (Method: link:name in nav)
            ['/gallery/django','Django'],
            ['/gallery/cybersecurity','Cyber Security'],
            ['/gallery/python','Python'],
        ],
    }
    return render(request,'projectgallery/index.html', context) #<--Include context to html file


def django(request):

    context = {
        'title':'Django',
        'contributor':'Pradipta Ramadhan',
        'directory':'gallery/templates/django/index.html',
    }
    return render(request,'django/index.html', context)

def cybersecurity(request):

    context = {
        'title':'Cyber Security',
        'contributor':'Pradipta Ramadhan',
        'directory':'gallery/templates/cybersecurity/index.html',
    }
    return render(request,'cybersecurity/index.html', context)

def python(request):

    context = {
        'title':'Python',
        'contributor':'Pradipta Ramadhan',
        'directory':'gallery/templates/python/index.html',
    }
    return render(request,'python/index.html', context)