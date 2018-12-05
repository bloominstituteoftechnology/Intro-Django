from rest_framework import serializers, viewsets
from notes import PersonalNote

class PersonalNoteSerializer(serializers.HyperlinkedModelSerializer):
	# Inner nested class
	class Meta:
		model = PersonalNote
		fields = ('title', 'content')

class PersonalNoteViewSet(viewsets.ModelViewSet):
	serilazer_class = PersonalNoteSerializer
	queryset = PersonalNote.objects.all()
	
