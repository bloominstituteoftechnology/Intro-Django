from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from .models import Music, PersonalMusic

def index(request):
    return HttpResponse("Music Inventory App!")
