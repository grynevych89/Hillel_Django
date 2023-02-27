from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from currency.models import Rate
from currency.forms import RateForm


def index(request):
    return render(request, 'currency/index.html')


def list_rates(request):
    rate = Rate.objects.order_by("-created")
    context = {
        'rate': rate
    }
    return render(request, 'currency/rates_list.html', context)


def rates_details(request, pk):
    rate = get_object_or_404(Rate, pk=pk)
    context = {
        'rate': rate
    }

    return render(request, 'currency/rates_details.html', context)


def rates_create(request):
    if request.method == 'POST':
        form = RateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/rate/list/')
    elif request.method == 'GET':
        form = RateForm()

        context = {
            'form': form
        }

        return render(request, 'currency/rates_create.html', context)


def rates_update(request, pk):
    rate = get_object_or_404(Rate, pk=pk)

    if request.method == 'POST':
        form = RateForm(request.POST, instance=rate)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/rate/list/')
    elif request.method == 'GET':
        form = RateForm(instance=rate)

        context = {
            'form': form,
        }

        return render(request, 'currency/rates_update.html', context)


def rates_delete(request, pk):
    rate = get_object_or_404(Rate, pk=pk)
    if request.method == 'POST':
        rate.delete()
        return HttpResponseRedirect('/rate/list/')
    elif request.method == 'GET':

        context = {
            'rate': rate,
        }

        return render(request, 'currency/rates_delete.html', context)
