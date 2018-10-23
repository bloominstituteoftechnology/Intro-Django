from django.contrib import admin
from .models import Apartment, DifferentApartment

class ApartmentAdmin(admin.ModelAdmin):
    readonly_fields=('created_at', 'last_modified')
# Register your models here.
admin.site.register(Apartment, ApartmentAdmin)
admin.site.register(DifferentApartment, ApartmentAdmin)

# You don't wanna commit that haha
# I know I changed my adress of the first apartment from 420 high st to
# 419 Lambda Proffesionalism Blvd
# rofl what's a "Lambda Professionalism"?
# idk it's just what the city named the street, beats me...
# I think I need multiple lines
# Yeah you're right