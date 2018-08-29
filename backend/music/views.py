from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from .models import Music, PersonalMusic

def index(request):
    return HttpResponse("Music Inventory App!")
    
@login_required
def view_all_music(request):
    music = Music.objects.all()
    context = {'music': music}
    return render(request, 'music/', context)
