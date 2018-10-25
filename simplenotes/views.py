from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth.models import User, Group
from django.core.exceptions import ValidationError
import json


@csrf_exempt
def register(request):
    data = json.loads(request.body)
    username = data['username']
    password = data['password']
    user = User(username=username)
    if len(username) <= 3:
        response = JsonResponse(
            {"error": "Username must be at least 3 characters."}, safe=True, status=500)
    elif len(password) <= 5:
        response = JsonResponse(
            {"error": "Password must be at least 5 characters."}, safe=True, status=500)
    else:
        try:
            user.validate_unique()
        except ValidationError:
            response = JsonResponse(
                {"error": "A user with that username already exists."}, safe=True, status=500)
        else:
            user.set_password(password)
            group = Group.objects.get(name='Basic User')
            group.user_set.add(user)
            user.save()
            response = JsonResponse({"key": str(user.auth_token)}, safe=True, status=201)
    return response

# Create your views here.
