from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect 
from django.shortcuts import render, get_object_or_404
# from django.template import loader
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.views.generic import ListView, DetailView
from .models import PersonalNote, Note

class IndexView(ListView):
    template_name = 'notes/index.html'
    context_object_name = 'latest_note_list'

    def get_queryset(self):
        """ Return the last five unpublished note"""
        return Note.objects.filter(created_on__lte=timezone.now()
        ).order_by('-created_on')[:10]

class ViewDetail(DetailView):
    model = Note
    template_name = 'notes/detail.html'


