from django import forms
from currency.models import Rate, RateSource


class RateForm(forms.ModelForm):

    class Meta:
        model = Rate
        fields = (
            'buy',
            'sale',
            'source',
            'currency'
        )


class SourceForm(forms.ModelForm):

    class Meta:
        model = RateSource
        fields = (
            'title',
        )
