import secrets

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordResetView, PasswordChangeView
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView

# from config.settings import EMAIL_HOST_USER
from users.forms import UserRegisterForm, UserRecoveryForm, UserProfileForm, UserPasswordChangeForm
from users.models import User


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    # def form_valid(self, form):
    #     user = form.save()
    #     user.is_active = False
    #     token = secrets.token_hex(16)
    #     user.token = token
    #     user.save()
    #     host = self.request.get_host()
    #     url = f'http:{host}/users/activate/{token}'
    #     send_mail(
    #         subject="подтвеждение почты",
    #         message=f'Для активации аккаунта перейдите по ссылке {url}',
    #         from_email=EMAIL_HOST_USER,
    #         recipient_list=[user.email],
    #         fail_silently=False,
    #     )
    #     return super().form_valid(form)


def activate(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse('users:login'))


class UserPasswordResetView(PasswordResetView):
    form_class = UserRecoveryForm
    template_name = 'users/password_reset_form.html'
    success_url = reverse_lazy('users:login')

    # def form_valid(self, form):
    #     if self.request.method == 'POST':
    #         user_email = self.request.POST.get('email')
    #         user = User.objects.filter(email=user_email).first()
    #         if user:
    #             new_password = secrets.token_hex(10)
    #             user.set_password(new_password)
    #             user.save()
    #             send_mail(
    #                 subject="Восстановление пароля",
    #                 message=f"Здравствуйте. Ваш пароль  изменен:\n"
    #                         f"Новый пароль: {new_password}\n"
    #                         f"Вы можете изменить его в своем профиле",
    #                 from_email=EMAIL_HOST_USER,
    #                 recipient_list=[user.email]
    #             )
    #
    #         return HttpResponseRedirect(reverse('users:login'))


class ProfileView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


class UserPasswordChangeView(PasswordChangeView):
    form_class = UserPasswordChangeForm
    success_url = reverse_lazy('users:password_change_done')
    template_name = 'users/password_change_form.html'
