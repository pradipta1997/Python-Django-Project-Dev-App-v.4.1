from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post



def index(request): #<--request itu sudah otomatis langsung membaca folder templates, yang mana sebelumnya sudah ter set di settings.py

    #QuerySet
    posts = Post.objects.all()  #<-- Query untuk mengambil semua data yang ada pada models class.
    #print(posts)    #<-- Debug untuk memastikan QuerySet yang dapat dilihat di terminal / Checker.

    context = { # <--Template Variable
        'title':'Blog',
        'contributor':'Pradipta Ramadhan',
        'directory':'templates/blog/index.html',
        'posts':posts,
        'nav':[ # <--Template Tags (Method: link:name in nav)
            ['/blog/news','News'],
            ['/blog/story','Story']
        ]
    }
    return render(request,'blog/index.html', context) #<--Include context to html file
    
def news(request):
    context = { # <--Template Variable
        'title':'   News',
        'contributor':'Jamal',
        'directory':'templates/news/index.html'
    }
    return render(request,'news/index.html', context) #<--Include context to html file

def story(request):
    context = { # <--Template Variable
        'title':'Story',
        'contributor':'Aburame',
        'directory':'templates/news/index.html'
    }
    return render(request,'story/index.html', context) #<--Include context to html file

def recent(request):
    return HttpResponse('<h1>This is blog->recent blog page</h1>')
