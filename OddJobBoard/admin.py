from django.contrib import admin
from .models import OddJobBoard
# Register your models here.
class OddJobBoardAdmin(admin.ModelAdmin):
	readonly_fields=('created_at', 'last_modified')

# Register your models here.
admin.site.register(OddJobBoard, OddJobBoardAdmin)
#admin.site.register(OddJobBoard)