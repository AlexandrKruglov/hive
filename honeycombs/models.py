from django.db import models

from users.models import User

NULLABLE = {"blank": True, "null": True}


class Honeycombs(models.Model):
    SCIENCE = 'Наука'
    GAME = 'Игры'
    FILM = 'Кино'
    MUSIC = 'Музыка'
    DUMP = 'Свалка'
    TOPIC_CHOICE = [
        (SCIENCE, 'Наука'),
        (GAME, 'Игры'),
        (FILM, 'Кино'),
        (MUSIC, 'Музыка'),
        (DUMP, 'Свалка'),
    ]
    name = models.CharField(max_length=100, verbose_name="заголовок")
    topic =  models.CharField(
        max_length=50,
        choices=TOPIC_CHOICE,
        default=DUMP,
        verbose_name="Тема")
    description = models.TextField(verbose_name="содержимое", **NULLABLE)
    image = models.ImageField(
        upload_to="image/", verbose_name="изображение", **NULLABLE
    )
    video = models.FileField(upload_to="video/", verbose_name="видео", **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="дата создания")
    count_views = models.IntegerField(default=0, verbose_name="просмотры")
    like = models.IntegerField(default=0, verbose_name="просмотры")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, **NULLABLE)
    paid_content = models.BooleanField(default=False, verbose_name="только по подписке")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "контент"
        verbose_name_plural = "контент"
        ordering = ("name",)
