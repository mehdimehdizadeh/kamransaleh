# Generated by Django 3.2.3 on 2023-03-04 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0003_subscribe'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=''),
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default=''),
        ),
        migrations.AddField(
            model_name='postcads',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]
