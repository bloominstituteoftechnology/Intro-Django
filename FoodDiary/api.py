from rest_framework import serializers, viewsets
from .models import PersonalEntry

class PersonalEntrySerializer(serializers.HyperlinkedModelSerializer):

	# Tells it what parts of the model we want to access
	class Meta:
		model = PersonalEntry
		fields = ('item', 'servings', 'was_enjoyed')

	def create(self, validated_data):
		user = self.context['request'].user
		entry = PersonalEntry.objects.create(user=user, **validated_data)
		return entry

class PersonalEntryViewSet(viewsets.ModelViewSet):
	serializer_class = PersonalEntrySerializer
	queryset = PersonalEntry.objects.none()

	def get_queryset(self):
		user = self.request.user

		if user.is_anonymous:
			return PersonalEntry.objects.none()
		else:
			return PersonalEntry.objects.filter(user=user)

