from rest_framework import serializers, viewsets
from .models import PersonalNote

class PersonalNoteSerializer(serializers.HyperlinkedModelSerializer):
    # BELOW DEFINES WHICH FIELDS TO SHOW
    class Meta:
        model = PersonalNote
        fields = ('title', 'content')

     ### BELOW OVERRIDES DEFAULT CREATE FUNCTIONALITY
     ### CREATE NEW PERSONAL NOTE THRU API , PASS IN VALIDATED DATA
    def create(self, validated_data):
         # BELOW DEBUGGER BREAKPOINT, ';' 2 LINES OF CODE IN 1 
         ##### import pdb; pdb.set_trace()
         # SEE PRINT OUT BELOW
        user = self.context['request'].user
         # BELOW (KWARGS)
        # note = PersonalNote.objects.create(**validated_data)
        #BELOW, PASSING IN CURRENT USER TO CREATE NOTE FROM UI /API
        note = PersonalNote.objects.create(user=user, **validated_data)
        return note


# BELOW DEFINES WHICH ROWS TO SHOW
class PersonalNoteViewSet(viewsets.ModelViewSet):
    # BELOW ATTACHES ABOVE SERIALIZER CLASS (TOP)
    serializer_class = PersonalNoteSerializer
    # BELOW DEFINES WHICH DATA TO RETURN
    # queryset = PersonalNote.objects.all()
    #ADDING BELOW TO FILTER OUT ONLY NOTES FOR
        #LOGGED IN USER, FROM /API/NOTES
    queryset = PersonalNote.objects.none()
    def get_queryset(self):
        user = self.request.user
        if user.is_anonymous:
            return PersonalNote.objects.none()
        else:
            return PersonalNote.objects.filter(user=user)











##################################################
# PYTHON DEBUGGER PRINT OUT 
     ### press 'l' for location, 'c' for continue
# > c:\users\tristan\documents\lambdaschool\cs11\github\w19d1-09172018-django\intro-django\notes\api.py(16)create()
# -> note = PersonalNote.objects.create(**validated_data)
 ### (Pdb) l
#  12         def create(self, validated_data):
#  14             import pdb; pdb.set_trace()
#  16  ->         note = PersonalNote.objects.create(**validated_data)
#  17             return note
#  20     class PersonalNoteViewSet(viewsets.ModelViewSet):
# (Pdb)
 ### (Pdb) self
# # PersonalNoteSerializer(context={'request': <rest_framework.request.Request object>, 'format': None, 'view': <notes.api.PersonalNoteViewSet object>}, data=<QueryDict: {'csrfmiddlewaretoken': ['gtjtkpHO70SlVPIiC5DjQS6xcc7Vb9QnvmsDnEUgdVOQdSoSWqR2AXONhk8zKa9M'], 'title': ['test2'], 'content': ['content test2']}>):
#     title = CharField(max_length=200)
#     content = CharField(allow_blank=True, required=False, style={'base_template': 'textarea.html'})
 ### (Pdb) validated_data
# {'title': 'test2', 'content': 'content test2'}
# (Pdb)
 ### (Pdb) self.context
# {'request': <rest_framework.request.Request object at 0x00000215DE31E080>, 'format': None, 'view': <notes.api.PersonalNoteViewSet object at 0x00000215DDF4E400>}
 ### (Pdb) self.context['request']
# <rest_framework.request.Request object at 0x00000215DE31E080>
 ### (Pdb) dir(self.context['request'])
# ['DATA', 'FILES', 'POST', 'QUERY_PARAMS', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattr__', '__getattribute__',
# '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_auth', '_authenticate', '_authenticator', '_content_type', '_data', '_default_negotiator', '_files', '_full_data', '_load_data_and_files', '_load_stream', '_not_authenticated', '_parse', '_request', '_stream', '_supports_form_parsing', '_user', 'accepted_media_type', 'accepted_renderer',
# 'auth', 'authenticators', 'content_type', 'csrf_processing_done', 'data', 'force_plaintext_errors', 'negotiator', 'parser_context', 'parsers', 'query_params', 'stream', 'successful_authenticator', 'user', 'version', 'versioning_scheme']
 ### (Pdb) self.context['request'].user
# <SimpleLazyObject: <User: admin>>
# (Pdb)