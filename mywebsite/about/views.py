from multiprocessing import context
from django.shortcuts import render

#Function index akan merequest file pada folder template (about.html)
def index(request):
    context = { # <--Template Variable
        'title':'About',
        'contributor':'Pradipta Ramadhan',
        'project':'Python Django 4.1',
        'directory':'templates/about.html',
        'nav':[
            ['/about','About'],
        ]
    }
    return render(request,'about.html', context) #<--Include context to html file
