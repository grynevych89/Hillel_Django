from django.urls import path
from .views import index, list_rates, rates_create, rates_details, rates_update, rates_delete

urlpatterns = [
    path('', index, name='index'),
    path('rate/list/', list_rates, name='rate_list'),
    path('rate/create/', rates_create, name='rate_create'),
    path('rate/details/<int:pk>/', rates_details),
    path('rate/update/<int:pk>/', rates_update),
    path('rate/delete/<int:pk>/', rates_delete),
]
