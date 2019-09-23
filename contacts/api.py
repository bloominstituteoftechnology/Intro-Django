from .models import Contact, PersonalContact
from rest_framework import serializers, viewsets

#CONTACTS

class ContactSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Contact
    fields = ('name', 'phone_number')
  
class ContactViewSet(viewsets.ModelViewSet):
  serializer_class = ContactSerializer
  queryset = Contact.objects.all()

  def get_queryset(self):
    user = self.request.user

    if user.is_anonymous:
      return PersonalContact.objects.none()

    else:
      return PersonalContact.objects.filter(user=user)

#PERSONAL CONTACTS

class PersonalContactSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = PersonalContact
    fields = ('name', 'phone_number')
  
class PersonalContactViewSet(viewsets.ModelViewSet):
  serializer_class = ContactSerializer
  queryset = PersonalContact.objects.all()

  def get_queryset(self):
    user = self.request.user

    if user.is_anonymous:
      return PersonalContact.objects.none()

    else:
      return PersonalContact.objects.filter(user=user)