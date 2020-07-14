from rest_framework import serializers, viewsets
from .models import PersonalProject
from django.contrib.auth.models import User,Permission
from rest_framework import permissions

class PersonalProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PersonalProject
        fields = ('id','project_title', 'created_at','last_modified','description','current_stage','plan_board','repo')
    def create(self, validated_data):
      user = self.context['request'].user
      note = PersonalProject.objects.create(user=user,**validated_data)
      return note
    

class PersonalProjectViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalProjectSerializer
    queryset = PersonalProject.objects.none()
    def get_queryset(self):
      user = self.request.user 
      if user.is_anonymous:
        return PersonalProject.objects.none()
      else:
        return PersonalProject.objects.filter(user=user)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'])
        user.set_password(validated_data['password'])
        user.user_permissions.add(Permission.objects.get(name='Can add personal project'))
        user.user_permissions.add(Permission.objects.get(name='Can change personal project'))
        user.user_permissions.add(Permission.objects.get(name='Can delete personal project'))        
        user.user_permissions.add(Permission.objects.get(name='Can view personal project'))
        user.save()
        return user


class CreateUserView(viewsets.ModelViewSet):
    model = User
    queryset = User.objects.none()

    permission_classes = [
        permissions.AllowAny # Or anon users can't register
    ]
    serializer_class = UserSerializer