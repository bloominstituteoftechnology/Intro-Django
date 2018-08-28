from rest_framework import routers
from notes.api import PersonalNoteViewset

router = routers.DefaultRouter()
router.register(r'notes', PersonalNoteViewset)
