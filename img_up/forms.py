from django import forms
from models import ImgUp

class DocumentForm(forms.ModelForm):
    class Meta:
        model = ImgUp
        fields = ('description', 'document', )
