from django import forms
from .models import *

class DocumentUploadForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['title', 'file']
class DocumentShareForm(forms.Form):
    signataire = forms.ModelChoiceField(
        queryset=CustomUser.objects.filter(role='SIGNATAIRE'),
        label="Sélectionner un signataire"
    )
    document_id = forms.IntegerField(widget=forms.HiddenInput())