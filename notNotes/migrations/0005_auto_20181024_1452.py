# Generated by Django 2.1.2 on 2018-10-24 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notNotes', '0004_personalnotnote'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notnote',
            name='title',
            field=models.CharField(default='default title', max_length=200),
        ),
    ]
