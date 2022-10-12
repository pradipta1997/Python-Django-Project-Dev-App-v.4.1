from turtle import title
from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255, blank=True)
    body = models.TextField()
    email = models.EmailField(default='example@web.com') # <-- default digunakan seperti halnya "placeholder" / bisa berguna juga disaat data sebelumnya belum memiliki field tertentu jadi disaat kita ingin menambahkan field lagi didata lama, maka field barunya harus di kasih nilai default.
    address = models.CharField(max_length=100, blank=True)
    postTime = models.DateTimeField(auto_now_add=True) # <-- hanya akan bisa dilihat di database waktu postnya, saat di terminal untuk "auto_now_add=True" ini ikuti saja instruksi yang diberikan agar berjalan atau bisa di migrate.
    categories = models.CharField(max_length=100, blank=True)
 
 
    # Ini adalah OOP Python untuk merubah nama Post pada admin agar sesuai dengan nama title
    def __str__(self):
        return "{}. {}".format(self.id ,self.title)