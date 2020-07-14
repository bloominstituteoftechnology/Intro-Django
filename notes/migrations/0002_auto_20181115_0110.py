# Generated by Django 2.1.3 on 2018-11-15 01:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalNote',
            fields=[
                ('note_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='notes.Note')),
                ('completed', models.BooleanField(default=False)),
            ],
            bases=('notes.note',),
        ),
        migrations.RemoveField(
            model_name='note',
            name='completed',
        ),
    ]
