# Generated by Django 4.1.1 on 2022-09-25 19:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='postTime',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]