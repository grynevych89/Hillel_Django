from source.models import Source
from source.forms import SourceForm
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class SourceListView(ListView):
    template_name = 'source/source_list.html'
    queryset = Source.objects.all()


class SourceDetailView(DetailView):
    queryset = Source.objects.all()
    template_name = 'source/source_details.html'


class SourceCreateView(CreateView):
    form_class = SourceForm
    template_name = 'source/source_create.html'
    success_url = reverse_lazy('source-list')


class SourceUpdateView(UpdateView):
    form_class = SourceForm
    template_name = 'source/source_update.html'
    success_url = reverse_lazy('source-list')
    queryset = Source.objects.all()


class SourceDeleteView(DeleteView):
    queryset = Source.objects.all()
    template_name = 'source/source_delete.html'
    success_url = reverse_lazy('source-list')
