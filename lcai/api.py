from rest_framework import serializers, viewsets, generics
# import django_filters.rest_framework
# from django_filters.rest_framework import DjangoFilterBackend
from .models import Home, Project, Evento, Miembro

# ''' FIRST APPROACH : START


class HomeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Home  # Table/Model to expose to from the API.
        fields = ('texto_es', 'texto_en')  # Select the Fields to expose.


class HomeViewSet(viewsets.ModelViewSet):
    serializer_class = HomeSerializer
    queryset = Home.objects.all()


class ProjectSerializar(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializar
    queryset = Project.objects.all()


class EventoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Evento
        fields = '__all__'


class EventoViewSet(viewsets.ModelViewSet):
    serializer_class = EventoSerializer
    queryset = Evento.objects.all()


class MiembroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Miembro
        fields = '__all__'


class MiembrosViewSet(viewsets.ModelViewSet):
    serializer_class = MiembroSerializer
    queryset = Miembro.objects.all()


# class DirectoraSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Miembro
#         fields = '__all__'


class DirectoraViewSet(viewsets.ModelViewSet):
    # serializer_class = DirectoraSerializer
    serializer_class = MiembroSerializer
    # queryset = Miembro.objects.all().filter(role='role_dir')
    queryset = Miembro.objects.none()

    def get_queryset(self):
        return Miembro.objects.all().filter(role='role_dir')


# class DirectoraView(generics.ListAPIView):
#     queryset = Miembro.objects.all()
#     serializer_class = DirectoraSerializer
#     filter_backends = (DjangoFilterBackend,)


# class InvestigadoresSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Miembro
#         fields = '__all__'


class InvestigadoresViewSet(viewsets.ModelViewSet):
    serializer_class = MiembroSerializer
    queryset = Miembro.objects.none()

    def get_queryset(self):
        return Miembro.objects.all().filter(role='role_inv')


# class DoctorandosSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Miembro
#         fields = '__all__'


class DoctorandosViewSet(viewsets.ModelViewSet):
    # serializer_class = DoctorandosSerializer
    serializer_class = MiembroSerializer
    queryset = Miembro.objects.none()

    def get_queryset(self):
        return Miembro.objects.all().filter(role='role_doc')


# class PhdThesisSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Miembro
#         fields = '__all__'


class PhdThesisViewSet(viewsets.ModelViewSet):
    # serializer_class = PhdThesisSerializer
    serializer_class = MiembroSerializer
    queryset = Miembro.objects.none()

    def get_queryset(self):
        return Miembro.objects.all().filter(role='role_phd')


# class ColaboradoresSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Miembro
#         fields = '__all__'


class ColaboradoresViewSet(viewsets.ModelViewSet):
    # serializer_class = ColaboradoresSerializer
    serializer_class = MiembroSerializer
    queryset = Miembro.objects.none()

    def get_queryset(self):
        return Miembro.objects.all().filter(role='role_col')

# ''' FIRST APPROACH : END
