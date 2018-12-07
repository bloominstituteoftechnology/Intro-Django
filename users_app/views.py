from django.shortcuts import render
from users_app.models import User
from users_app.models import Note, PersonalNote
from django.http import HttpResponse
#home page view
def index(request):
    return HttpResponse("""
         <a href="https://djorn-brian-ruff.herokuapp.com/admin/">Admin</a>
    """)
    #render(request, 'users/index.html')

#users view
def users(request):

    user_list = User.objects.order_by('first_name')
    user_dict = {'users':user_list}
    return render(request, 'users/users.html', context=user_dict)


#get rid of no such object error:
#first: pip install pylint-django
#after that open VS /preferences/settings/and insert:
#{"python.linting.pylintArgs": [
#     "--load-plugins=pylint_django"


# ], }
# in users setting/vs 
