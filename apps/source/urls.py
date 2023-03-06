from django.urls import path
from source.views import (
    SourceListView,
    SourceCreateView,
    SourceDetailView,
    SourceUpdateView,
    SourceDeleteView
)

urlpatterns = [
    path('source/list/', SourceListView.as_view(), name='source-list'),
    path('source/create/', SourceCreateView.as_view(), name='source-create'),
    path('source/details/<int:pk>/', SourceDetailView.as_view(), name='source-detail'),
    path('source/update/<int:pk>/', SourceUpdateView.as_view(), name='source-update'),
    path('source/delete/<int:pk>/', SourceDeleteView.as_view(), name='source-delete'),
]
