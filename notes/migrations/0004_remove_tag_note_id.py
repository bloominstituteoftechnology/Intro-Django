# Generated by Django 2.1.1 on 2018-09-17 19:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_tag_note_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='note_id',
        ),
    ]
