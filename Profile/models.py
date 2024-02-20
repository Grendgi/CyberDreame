from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/')
    date_of_registration = models.DateTimeField(auto_now_add=True)
    last_visit = models.DateTimeField(auto_now=True)
    bio = models.TextField(blank=True)
    # Дополнительные поля, если необходимы


class GameProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='game_profiles')
    game_name = models.CharField(max_length=100, verbose_name='Игра или сервис')
    character_name = models.CharField(max_length=100, verbose_name='Имя персонажа или ссылка на профиль')

    def __str__(self):
        return f'{self.game_name}: {self.character_name}'