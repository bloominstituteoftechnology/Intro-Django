# Generated by Django 2.1 on 2018-08-28 17:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0004_auto_20180828_1045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalnote',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
