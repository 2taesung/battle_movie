# Generated by Django 3.2.3 on 2021-05-21 00:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0002_alter_movie_poster_path'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='community',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='community',
            name='updated_at',
        ),
    ]