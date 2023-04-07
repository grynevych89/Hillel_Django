from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView, RedirectView, CreateView
from accounts.forms import UserSignUpForm
from django.contrib.auth import get_user_model


class ProfileView(LoginRequiredMixin, UpdateView):
    template_name = 'registration/profile.html'
    success_url = reverse_lazy('index')
    queryset = get_user_model().objects.all()
    fields = (
        'first_name',
        'last_name',
        'email',
        'phone',
        'avatar',
    )

    def get_object(self, queryset=None):
        return self.request.user


class UserSignUpView(CreateView):
    queryset = get_user_model().objects.all()
    template_name = 'registration/regist.html'
    success_url = reverse_lazy('login')
    form_class = UserSignUpForm


class UserActivateView(RedirectView):
    pattern_name = 'login'

    def get_redirect_url(self, *args, **kwargs):
        unique_id = kwargs.pop('unique_id')

        user = get_user_model().objects.filter(unique_id=unique_id).only('id').first()
        if user is not None:
            user.is_active = True
            user.save(update_fields=['is_active'])

        url = super().get_redirect_url(*args, **kwargs)
        return url
