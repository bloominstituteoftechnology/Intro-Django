from django.shortcuts import render
from django.http import HttpResponse

# Index View
def index(request):
    return HttpResponse("This is the index route of the polls app")
