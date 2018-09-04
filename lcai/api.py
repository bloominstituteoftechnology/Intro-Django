from rest_framework import serializers, viewsets
from .models import Home, Miembro


class HomeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Home  # Table/Model to expose to from the API.
        fields = ('texto_es', 'texto_en')  # Select the Fields to expose.


class HomeViewSet(viewsets.ModelViewSet):
    serializer_class = HomeSerializer
    queryset = Home.objects.all()

    # def get_queryset(self):
    #     user = self.request.user

    #     if user.is_anonymous:
    #         return PersonalNote.objects.none()
    #     else:
    #         return PersonalNote.objects.filter(user=user)


class DirectoraSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Miembro
        fields = '__all__'


class DirectoraViewSet(viewsets.ModelViewSet):
    serializer_class = DirectoraSerializer
    queryset = Miembro.objects.all().filter(role='role_dir')


class InvestigadoresSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Miembro
        fields = '__all__'


class InvestigadoresViewSet(viewsets.ModelViewSet):
    serializer_class = DirectoraSerializer
    queryset = Miembro.objects.all().filter(role='role_inv')


class DoctorandosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Miembro
        fields = '__all__'


class DoctorandosViewSet(viewsets.ModelViewSet):
    serializer_class = DoctorandosSerializer
    queryset = Miembro.objects.all().filter(role='role_doc')


class PhdThesisSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Miembro
        fields = '__all__'


class PhdThesisViewSet(viewsets.ModelViewSet):
    serializer_class = PhdThesisSerializer
    queryset = Miembro.objects.all().filter(role='role_phd')


class ColaboradoresSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Miembro
        fields = '__all__'


class ColaboradoresViewSet(viewsets.ModelViewSet):
    serializer_class = ColaboradoresSerializer
    queryset = Miembro.objects.all().filter(role='role_col')
