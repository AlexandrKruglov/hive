from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeDoneView
from django.urls import path, reverse_lazy

from users.apps import UsersConfig
from users.views import UserPasswordResetView, ProfileView, RegisterView, UserPasswordChangeView

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='users/logout.html', http_method_names=["post", "get", "options"]), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('password-reset/', UserPasswordResetView.as_view(template_name="users/password_reset_form.html"),
         name='password-reset'),
    path('password-change', UserPasswordChangeView.as_view(template_name="users/password_change_form.html"),
         name='password-change'),
    path('password-change/done/', PasswordChangeDoneView.as_view(template_name="users/password_change_done.html"),
         name="password_change_done")
]
