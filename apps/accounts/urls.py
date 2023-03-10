from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from accounts.views import ProfileView
from accounts import views

urlpatterns = [
    path('profile/', ProfileView.as_view(), name='profile'),
    path('regist', views.register_request, name='regist'),
    path('password_change/', auth_views.PasswordChangeView.as_view(
        template_name='registration/password_change.html',
        success_url=reverse_lazy('profile')
    ), name='password_change'),
]
