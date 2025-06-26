from django.db import models
from django.contrib.auth.models import User # Если хотите связать пост с пользователем

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержание")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        ordering = ['-created_at'] # Сортировка по убыванию даты создания

    def __str__(self):
        return self.title[:50] # Для удобного отображения в админке