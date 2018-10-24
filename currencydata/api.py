from rest_framework import serializers
from .models import PersonalCurrencydata

class PersonalCurrencydataSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = PersonalCurrencydata
        fields = ('date', 'the_open', 'the_high', 'the_low', 'the_close', 'bar_type', 'created_at', 'last_modified')
        
class PersonalCurrencydataViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalCurrencydataSerializer
    queryset = PersonalCurrencydata.objects.none()
    def get_queryset(self):
        import pdb; pdb.set_trace()

        logged_in_user = self.request.user

        if logged_in_user.is_anonymous:
            return PersonalNote.objects.none()
        else:
            return PersonalNote.objects.filter(user=logged_in_user)
        
