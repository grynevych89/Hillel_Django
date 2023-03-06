from contacts.models import ContactUs
from contacts.forms import ContactUsForm
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class ContactUsListView(ListView):
    template_name = 'contacts/contacts_list.html'
    queryset = ContactUs.objects.all()


class ContactUsDetailView(DetailView):
    queryset = ContactUs.objects.all()
    template_name = 'contacts/contacts_details.html'


class ContactUsCreateView(CreateView):
    form_class = ContactUsForm
    template_name = 'contacts/contacts_create.html'
    success_url = reverse_lazy('contact-list')


class ContactUsUpdateView(UpdateView):
    form_class = ContactUsForm
    template_name = 'contacts/contacts_update.html'
    success_url = reverse_lazy('contact-list')
    queryset = ContactUs.objects.all()


class ContactUsDeleteView(DeleteView):
    queryset = ContactUs.objects.all()
    template_name = 'contacts/contacts_delete.html'
    success_url = reverse_lazy('contact-list')
