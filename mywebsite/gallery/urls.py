from django.urls import path

from . import views

urlpatterns = [
    path('', views.index), # <--Dalam include urls (dari url app ke-> url project, nama route-nya tidak perlu diisi lagi) agar tidak double route.
    path('django/', views.django),
    path('cybersecurity/', views.cybersecurity),
    path('python/', views.python),
]