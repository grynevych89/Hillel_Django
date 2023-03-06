from django import forms
from contacts.models import ContactUs


class ContactUsForm(forms.ModelForm):

    class Meta:
        model = ContactUs
        fields = (
            'id',
            'subject',
            'email_from',
            'message',
        )
