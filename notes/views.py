from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("""
        <b>1.</b> <a href="http://127.0.0.1:8000/admin/">Admin</a><br><br>
        <b>2.</b> <a href="http://127.0.0.1:8000/api/">API</a><br><br>
        <b>3.</b> <a href="http://127.0.0.1:8000/api-token-auth/">API Token Auth</a>
    """)