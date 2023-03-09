from django import forms
from contacts.models import ContactUs


class ContactUsForm(forms.ModelForm):

    class Meta:
        model = ContactUs
        fields = (
            'name',
            'subject',
            'email_from',
            'message',
        )
