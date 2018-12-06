from django.shortcuts import render

# BUG FIX ATTEMPT

# from django.db.utils import OperationalError
# format_list = [('', '(all)')]
# geom_type_list = [('', '(all)')]

# try:
#     format_list.extend([(i[0],i[0])
#         for i in Format.objects.values_list('name')])
#     geom_type_list.extend([(i[0],i[0])
#         for i in Geom_type.objects.values_list('name')])
# except OperationalError:
#     pass

# Create your views here.
