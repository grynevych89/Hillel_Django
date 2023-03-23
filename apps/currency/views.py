from currency.models import Rate
from currency.forms import RateForm
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class RateListView(ListView):
    template_name = 'currency/rates_list.html'
    queryset = Rate.objects.all().select_related('source')


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
