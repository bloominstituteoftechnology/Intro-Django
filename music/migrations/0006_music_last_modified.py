# Generated by Django 2.1 on 2018-08-28 17:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0005_auto_20180828_0919'),
    ]

    operations = [
        migrations.AddField(
            model_name='music',
            name='last_modified',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
