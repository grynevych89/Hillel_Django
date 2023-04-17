from currency.models import Rate
from currency.forms import RateForm
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django_filters.views import FilterView
from currency.filters import RateFilter


class RateListView(FilterView):
    template_name = 'currency/rates_list.html'
    queryset = Rate.objects.all().select_related('source')
    paginate_by = 3
    filterset_class = RateFilter

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_pagination'] = '&'.join(
            f'{key}={value}' for key, value in self.request.GET.items() if key != 'page'
        )
        return context


class RateDetailView(LoginRequiredMixin, DetailView):
    queryset = Rate.objects.all()
    template_name = 'currency/rates_details.html'


class RateCreateView(CreateView):
    form_class = RateForm
    template_name = 'currency/rates_create.html'
    success_url = reverse_lazy('rate-list')


class RateUpdateView(UserPassesTestMixin, UpdateView):
    form_class = RateForm
    template_name = 'currency/rates_update.html'
    success_url = reverse_lazy('rate-list')
    queryset = Rate.objects.all()

    def test_func(self):
        return self.request.user.is_superuser


class RateDeleteView(UserPassesTestMixin, DeleteView):
    queryset = Rate.objects.all()
    template_name = 'currency/rates_delete.html'
    success_url = reverse_lazy('rate-list')

    def test_func(self):
        return self.request.user.is_superuser
