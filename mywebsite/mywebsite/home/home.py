from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render

def index(request):

    context = { #Agar bisa menggunakan template variable
        'title':'The Project',
        'contributor':'Pradipta Ramadhan',
        'nav':[
            ['/','Home'],
            ['/blog','Blog'],
            ['/about','About'],
            ['/contact','Contact']
        ]
    }
    return render(request,'index.html', context) #Load context (template variable)

# def index(request):
#     return HttpResponse("Home Page")