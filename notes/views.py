from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("""
        <b>1.</b> <a href="https://notes-huthman.herokuapp.com/admin/">Admin</a><br><br>
        <b>2.</b> <a href="https://notes-huthman.herokuapp.com/api/">API</a><br><br>
        <b>3.</b> <a href="https://notes-huthman.herokuapp.com/api-token-auth/">API Token Auth</a>
    """)