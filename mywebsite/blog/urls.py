from django.urls import path

from . import views
# from blog import views as blogViews # <-- url using app

urlpatterns = [
    path('recent/',views.recent),
    path('', views.index), # <--Dalam include urls (dari url app ke-> url project, nama route-nya tidak perlu diisi lagi) agar tidak double route.
    path('news/', views.news),
    path('story/', views.story),
]