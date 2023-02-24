from django.shortcuts import render
from currency.models import Rate


def index(request):
    rate = Rate.objects.order_by("-created")
    return render(request, 'currency/index.html', context={
        'rate': rate,
    })
