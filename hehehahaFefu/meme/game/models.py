from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class Userdata(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    games = models.PositiveIntegerField(default=0)
    score = models.PositiveIntegerField(default=0)
    first_places = models.PositiveIntegerField(default=0)


# class Lobby(models.Model):
#     lobby = models.BigAutoField(primary_key=True)
#     lobby_name = models.CharField(max_length=25)
#     round_time = models.PositiveSmallIntegerField(default=30)
#     max_players = models.PositiveSmallIntegerField(default=3)
#     is_private = models.BooleanField(default=False)
#
#
# class Players(models.Model):
#     lobby = models.OneToOneField(Lobby, on_delete=models.CASCADE)
#     user_nickname = models.CharField(max_length=20)
#     is_creator = models.BooleanField(default=False)
#     score = models.PositiveSmallIntegerField(default=0)
#
#     def save(self, *args, **kwargs):
#         if Players.objects.count() < Lobby.max_players:
#             super().save(*args, **kwargs)
#
