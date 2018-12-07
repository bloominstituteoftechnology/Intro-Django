from rest_framework import serializers, viewsets
from .models import Note, PersonalNote

class PersonalNoteSerializer(serializers.HyperlinkedModelSerializer):
	# Inner nested class
	class Meta:
		model = PersonalNote
		fields = ('title', 'content')

	def create(self, validated_data):
		# import pdb; pdb.set_trace()
		user = self.context['request'].user
		note = PersonalNote.objects.create(user=user,**validated_data)
		print(f"New PersonalNote initialized by {user}")
		return note

class PersonalNoteViewSet(viewsets.ModelViewSet):
	serializer_class = PersonalNoteSerializer
	queryset = Note.objects.none()

	def get_queryset(self):
		user = self.request.user

		if user.is_anonymous:
			return PersonalNote.objects.none()
		else:
			return PersonalNote.objects.filter(user=user)



