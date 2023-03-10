from django import forms
from documents.models import Department, Document


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['title', 'file', 'department']
