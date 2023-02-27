from django.urls import path
from .views import list_source, source_create, source_details, source_update, source_delete

urlpatterns = [
    path('/list/', list_source, name='source_list'),
    path('/create/', source_create, name='source_create'),
    path('/details/<int:pk>/', source_details),
    path('/update/<int:pk>/', source_update),
    path('/delete/<int:pk>/', source_delete),
]
