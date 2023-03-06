from django.urls import path
from contacts.views import (
    ContactUsListView,
    ContactUsCreateView,
    ContactUsDetailView,
    ContactUsUpdateView,
    ContactUsDeleteView,
)

urlpatterns = [
    path('contact/list/', ContactUsListView.as_view(), name='contact-list'),
    path('contact/create/', ContactUsCreateView.as_view(), name='contact-create'),
    path('contact/details/<int:pk>/', ContactUsDetailView.as_view(), name='contact-detail'),
    path('contact/update/<int:pk>/', ContactUsUpdateView.as_view(), name='contact-update'),
    path('contact/delete/<int:pk>/', ContactUsDeleteView.as_view(), name='contact-delete'),
]
