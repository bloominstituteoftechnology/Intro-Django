# Generated by Django 2.1.2 on 2018-10-25 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodJournal', '0004_personalnote'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='title',
            field=models.CharField(default='title', max_length=300),
        ),
    ]
