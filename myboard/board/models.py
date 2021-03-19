from django.db import models
from django.contrib.auth.models import User


class Person(models.Model):
    pass


class Category(models.Model):
    name = models.CharField('категория', max_length=64)

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    def __str__(self):
        return self.name


class Board(models.Model):
    pass


class Comment(models.Model):
    pass
