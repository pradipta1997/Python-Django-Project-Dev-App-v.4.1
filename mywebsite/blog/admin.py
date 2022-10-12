from django.contrib import admin

# Register your models here.

from . models import Post # <-- Untuk import file models.py dengan class Post.

admin.site.register(Post) # <-- Untuk mengregister class Post sebagai admin.

# FUNGSI-NYA FILE INI ADALAH UNTUK MENREGISTRASIKAN
# FILES models.py YANG ADA DIDALAM APP blog, SUPAYA
# KITA DAPAT MELAKUKAN KONFIGURASI DI 
# http://127.0.0.1:8000/admin/blog/post/
