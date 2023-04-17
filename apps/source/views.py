from source.models import Source
from source.forms import SourceForm
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django_filters.views import FilterView
from source.filters import SourceFilter


class SourceListView(FilterView):
    template_name = 'source/source_list.html'
    queryset = Source.objects.all()
    paginate_by = 4
    filterset_class = SourceFilter

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_pagination'] = '&'.join(
            f'{key}={value}' for key, value in self.request.GET.items() if key != 'page'
        )
        return context


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
