# from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from notes.models import PersonalNote

# Create your views here.
def notes(request):
    notes_list = PersonalNote.objects.all()
    template = loader.get_template("notes.html")
    context = {"notes": notes_list}
    return HttpResponse(template.render(context, request))

