# from django.shortcuts import render
from django.http import HttpResponse


def index(reques):
    return HttpResponse('Hi there, just playing and messing around with Django!')
