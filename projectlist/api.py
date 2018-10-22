from rest_framework import serializers, viewsets


class PersonalProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PersonalProject
        fields = ('project_title', 'created_at','last_modified','description','current_stage','plan_board','repo','user')

class PersonalProjectViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalProjectSerializer
    queryset = PersonalProject.objects.all()
