# Generated by Django 2.1.2 on 2018-10-22 21:59

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='user_id',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, to='notes.User'),
            preserve_default=False,
        ),
    ]
