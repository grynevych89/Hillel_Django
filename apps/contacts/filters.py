import django_filters

from contacts.models import ContactUs


class ContactsFilter(django_filters.FilterSet):
    class Meta:
        model = ContactUs
        fields = ['name', 'email_from']


class ContactsFilterApi(django_filters.FilterSet):
    class Meta:
        model = ContactUs
        fields = {
            'name': ('exact', ),
            'email_from': ('exact', ),
            'subject': ('exact', ),
            'created': ('exact', ),
        }
