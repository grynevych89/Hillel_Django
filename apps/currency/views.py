from django.shortcuts import render
from currency.models import Rate, ContactUs


def index(request):
    rate = Rate.objects.order_by("-created")
    contact_us = ContactUs.objects.all()
    return render(request, 'index.html', context={
        'rate': rate,
        'contact_us': contact_us,
    })
