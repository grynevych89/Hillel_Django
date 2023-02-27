from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from source.models import Source
from source.forms import SourceForm


def list_source(request):
    source = Source.objects.all()
    return render(request, 'source/source_list.html', context={'source': source, })


def source_details(request, pk):
    source = get_object_or_404(Source, pk=pk)
    return render(request, 'source/source_details.html', context={'source': source, })


def source_create(request):
    if request.method == 'POST':
        source_form = SourceForm(request.POST)
        if source_form.is_valid():
            source_form.save()
            return HttpResponseRedirect('/source/list/')
    elif request.method == 'GET':
        source_form = SourceForm()
    return render(request, 'source/source_create.html', context={'source_form': source_form, })


def source_update(request, pk):
    source = get_object_or_404(Source, pk=pk)

    if request.method == 'POST':
        source_form = SourceForm(request.POST, instance=source)
        if source_form.is_valid():
            source_form.save()
            return HttpResponseRedirect('/source/list/')
    elif request.method == 'GET':
        source_form = SourceForm(instance=source)
    return render(request, 'source/source_update.html', context={'source_form': source_form, })


def source_delete(request, pk):
    source = get_object_or_404(Source, pk=pk)
    if request.method == 'POST':
        source.delete()
        return HttpResponseRedirect('/source/list/')
    elif request.method == 'GET':
        return render(request, 'source/source_delete.html', context={'source': source, })
