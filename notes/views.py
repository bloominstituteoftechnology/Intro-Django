from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("""
        <b>1.</b> <a href="https://djorn-brian-ruff.herokuapp.com/admin/">Admin</a><br><br>
        <b>2.</b> <a href="https://djorn-brian-ruff.herokuapp.com/api/">API</a><br><br>
        <b>3.</b> <a href="https://djorn-brian-ruff.herokuapp.com/api-token-auth/">API Token Auth</a>
    """)