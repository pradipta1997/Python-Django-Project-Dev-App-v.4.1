from django.urls import path

from . import views

#Masuk ke file views lalu cari function yang namanya index
urlpatterns = [
    path('', views.index), # <--Dalam include urls (dari url app ke-> url project, nama route-nya tidak perlu diisi lagi) agar tidak double route.
]