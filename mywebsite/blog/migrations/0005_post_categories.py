# Generated by Django 4.1.1 on 2022-09-26 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_posttime'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='categories',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]