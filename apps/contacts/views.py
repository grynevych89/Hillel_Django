from django.shortcuts import render
from contacts.models import ContactUs


def contacts(request):
    contact_us = ContactUs.objects.all()
    return render(request, 'contacts/contacts.html', context={
        'contact_us': contact_us,
    })
