from django import forms
from .models import Graph

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = Graph
        fields = [
            "file",
        ]