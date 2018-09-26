from django.shortcuts import render
from django.http import HttpResponse
from notes.models import Note, PersonalNote

# Create your views here.


def index(request):
    notes_list = Note.objects.order_by('created_at')
    date_dict = {'note': notes_list}
    return render(request, "notes/index.html", context=date_dict)


def obtain_auth_token():
    pass
