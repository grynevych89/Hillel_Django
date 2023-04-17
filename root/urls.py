from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Grynevych API",
        default_version='v1',
        description="Home Works",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="grynevych89@gmail.com"),
        license=openapi.License(name="by Grynevych"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

v1_url_patterns = [
    path('v1/api/currency/', include('currency.api.v1.urls')),
    path('v1/api/source/', include('source.api.v1.urls')),
    path('v1/api/contacts/', include('contacts.api.v1.urls')),
]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),

    path('__debug__/', include('debug_toolbar.urls')),

    path('rates/', include('currency.urls')),
    path('source/', include('source.urls')),
    path('contacts/', include('contacts.urls')),

    path('api/', include('accounts.api.urls')),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('', TemplateView.as_view(template_name='index.html'), name='index'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += v1_url_patterns
