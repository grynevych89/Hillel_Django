from contacts.models import ContactUs
from contacts.forms import ContactUsForm
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django_filters.views import FilterView
from contacts.filters import ContactsFilter
# from root import settings


class ContactUsListView(FilterView):
    template_name = 'contacts/contacts_list.html'
    queryset = ContactUs.objects.all()
    paginate_by = 2
    filterset_class = ContactsFilter

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_pagination'] = '&'.join(
            f'{key}={value}' for key, value in self.request.GET.items() if key != 'page'
        )
        return context


class ContactUsDetailView(DetailView):
    queryset = ContactUs.objects.all()
    template_name = 'contacts/contacts_details.html'


class ContactUsCreateView(CreateView):
    template_name = 'contacts/contacts_create.html'
    success_url = reverse_lazy('contact-list')
    model = ContactUs
    fields = (
        'name',
        'email_from',
        'subject',
        'message'
    )

    def _send_mail(self):
        subject = 'User ContactUs'
        # recipient = settings.DEFAULT_FROM_EMAIL
        message = f'''
        Спасибо за обращение! Мы свяжемся с Вами в ближайшее время.
        Ваши введенные данны из формы:
            Request from: {self.object.name},
            Reply to email: {self.object.email_from},
            Subject: {self.object.subject},
            Body: {self.object.message}
        '''
        from contacts.tasks import send_mail
        send_mail.delay(subject, message)
        # send_mail.apply_async(args=[subject, message])
        '''
        0 - 8.59 | 9.00 - 19.00 | 19.01 23.59
           9.00  |    send      | 9.00 next day
        '''
        # from datetime import datetime, timedelta
        # send_mail.apply_async(
        #     kwargs={'subject': subject, 'message': message},
        #     # countdown=20
        #     # eta=datetime(2023, 3, 28, 20, 49, 0)
        # )

    def form_valid(self, form):
        redirect = super().form_valid(form)
        self._send_mail()
        return redirect


class ContactUsUpdateView(UpdateView):
    form_class = ContactUsForm
    template_name = 'contacts/contacts_update.html'
    success_url = reverse_lazy('contact-list')
    queryset = ContactUs.objects.all()


class ContactUsDeleteView(DeleteView):
    queryset = ContactUs.objects.all()
    template_name = 'contacts/contacts_delete.html'
    success_url = reverse_lazy('contact-list')
