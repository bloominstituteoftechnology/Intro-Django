# Generated by Django 2.1.1 on 2018-09-17 22:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0011_illustrate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='year_published',
        ),
    ]
