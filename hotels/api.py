from rest_framework import serializers, viewsets
from .models import  DifferentApartment

class DifferentApartmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DifferentApartment
        fields = ( 'Name', 'Phone', 'Website', 'Email', 'Address', 'Zip', 'distance')

    def create(self, validated_data):
        # return apartment
        # import pdb; pdb.set_trace()  # Start the debugger here
        user = self.context["request"].user # <-- This gets you the user_id...but you have to do something with it Oh well we need to hmmmmmmmm Hint: look at the readme yah doing that now
        apartment = DifferentApartment.objects.create(user=user, **validated_data)
        # lol ummmmm give it timeeeee rofl
        # i'd give you a line number but it's not showing up in my screen...but i have a better idea. look at `day3.md` please and find my cursor. i highlighted it
        # so you got this user up here in line 13. what are you going to do with it?
        # I think it's to set the user in when we are doing the post from the api instead of admin pannel
        # but I don't really know the differrence 
        # Are we setting or just reading? when you did the debug in line 12, you examined what
        # information was being passed along in self, right? Not really I dind't really know where to check it and was 
        # kinda rushing to catch up end of the day and the next line or two in the git discrip was like you would see the code is
        # this so first and formost probably I should look at this debugger 
        # day 4 is kind of short, but i can give you the cliff notes version 
        # that would be best, but the cliff notes version is that somewhere in self, there is information about the user doing the request
        # remember, you are getting an error saying "user_id cannot be null" or whatever, so you need to save the user (more specifically their id)
        # along with the information they are saving.
        # question is, where are you going to get this id?
        return apartment


class DifferentApartmentViewSet(viewsets.ModelViewSet):
    serializer_class = DifferentApartmentSerializer
    queryset = DifferentApartment.objects.none()

    def get_queryset(self):
        user = self.request.user

        if user.is_anonymous:
            return DifferentApartment.objects.none()
        else:
            return DifferentApartment.objects.filter(user=user)
