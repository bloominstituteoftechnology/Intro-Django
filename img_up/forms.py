from django import forms
from .models import Epilepsy

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Epilepsy
        fields = ('description', 'document', )
