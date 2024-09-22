from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    username = None
    email = models.EmailField(verbose_name='email')
    # company = models.CharField(max_length=35, verbose_name='company', **NULLABLE)
    phone = models.CharField(unique=True, max_length=35, verbose_name='телефон')
    nickname = models.CharField(max_length=50, unique=True, verbose_name='ник')
    avatar = models.ImageField(upload_to="avatar/", default="avatar/new_preview.jpg")
    # token = models.CharField(max_length=100, verbose_name='token', **NULLABLE)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"
        # permissions = [
        #     ('deactivate_user', 'Can deactivate user'),
        #     ('view_all_users', 'Can view all users'),
        # ]


class Payments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')
    date_pay = models.DateField(verbose_name='дата оплаты')
    purpose = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='подписка на пользователя')
    summ = models.PositiveIntegerField(verbose_name='сумма оплаты')
    link = models.URLField(max_length=400, **NULLABLE, verbose_name='ссылка на оплату')
    session_id = models.CharField(max_length=200, **NULLABLE, verbose_name='id session')

    def __str__(self):
        return f'{self.user} - {self.course if self.course else self.lesson}'

    class Meta:
        verbose_name = 'платеж'
        verbose_name_plural = 'платежи'


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')
    subscribe_to_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='подписка на данного пользователя')

    def __str__(self):
        return f'{self.user} - {self.course} '

    class Meta:
        verbose_name = 'подписка'
        verbose_name_plural = 'подписки'