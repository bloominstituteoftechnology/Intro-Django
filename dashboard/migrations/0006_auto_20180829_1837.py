# Generated by Django 2.1 on 2018-08-29 22:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_auto_20180829_1814'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectmanager',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projectmanager',
            name='last_modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='sprintstatus',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sprintstatus',
            name='last_modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
