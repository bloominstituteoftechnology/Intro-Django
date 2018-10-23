# Generated by Django 2.1.2 on 2018-10-23 22:16

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('author', models.CharField(max_length=200)),
                ('content', models.TextField(blank=True)),
            ],
        ),
    ]
