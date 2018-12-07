from rest_framework import serializers, viewsets
from .models import PersonalQuote, Quote

class PersonalQuoteSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:	
		model = PersonalQuote
		fields = ('Author', 'Quote')
	def create(self, validated_data):
		user = self.context['request'].user
		note = PersonalQuote.objects.create(user=user, **validated_data)
		return Quote



class PersonalQuoteViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalQuoteSerializer
    queryset = Quote.objects.none()
    def get_queryset(self):
        user = self.request.user

        if user.is_anonymous:
            return PersonalQuote.objects.none()
        else:
            return PersonalQuote.objects.filter(user=user)