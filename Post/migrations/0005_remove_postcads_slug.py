# Generated by Django 3.2.3 on 2023-03-04 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0004_auto_20230304_1640'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postcads',
            name='slug',
        ),
    ]
