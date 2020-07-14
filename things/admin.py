from django.contrib import admin
from things.models import Thing, PersonalThing
# Register your models here.


class ThingAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'last_modified')


admin.site.register(Thing, ThingAdmin)
admin.site.register(PersonalThing, ThingAdmin)

