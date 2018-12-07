from rest_framework import serializers, viewsets
from .models import Entry

class EntrySerializer(serializers.HyperlinkedModelSerializer):

	# Tells it what parts of the model we want to access
	class Meta:
		model = Entry
		fields = ('item', 'servings', 'was_enjoyed')

class EntryViewSet(viewsets.ModelViewSet):
	serialzer_class = EntrySerializer
	queryset = EntryNote.objects.all()
