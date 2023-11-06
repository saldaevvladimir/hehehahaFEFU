from django.db import models


class User(models.Model):
    login = models.CharField(max_length=25, blank=False)
    password = models.CharField(max_length=25, blank=False)

    def __str__(self):
        return f'{self.login}'


