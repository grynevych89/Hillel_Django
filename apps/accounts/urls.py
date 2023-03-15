from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from accounts.views import ProfileView, UserSignUpView, UserActivateView

app_name = 'account'


urlpatterns = [
    path('profile/', ProfileView.as_view(), name='profile'),
    path('password_change/', auth_views.PasswordChangeView.as_view(
        template_name='registration/password_change.html',
        success_url=reverse_lazy('account:profile')
    ), name='password_change'),
    path('regist/', UserSignUpView.as_view(), name='regist'),
    path('activate/<uuid:unique_id>/', UserActivateView.as_view(), name='activate'),
]
