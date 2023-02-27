from django import forms
from source.models import Source


class SourceForm(forms.ModelForm):

    class Meta:
        model = Source
        fields = (
            'name',
            'text',
            'source_url',
            'price'
        )
