from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField('категория', max_length=64)

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    def __str__(self):
        return self.name


class Board(models.Model):
    category = models.ForeignKey(Category, verbose_name='категория', on_delete=models.CASCADE)
    name = models.CharField('заголовок', max_length=80)
    description = models.TextField('текст', max_length=500)
    image = models.ImageField('изображение', upload_to='images/items/%Y/%m/%d')
    content = models.TextField('дополнительный контент', null=True)
    publish = models.DateTimeField(auto_now_add=True, verbose_name='online: ')
    created = models.DateTimeField(default=timezone.now, verbose_name='дата создания: ')

    def __str__(self):
        return f'{self.category}, {self.name}, {self.description[:50]}, {self.image}, {self.content}, {self.created}'

    class Meta:
        verbose_name = 'объявление'
        verbose_name_plural = 'объявления'


class Comment(models.Model):
    comment = models.TextField('комментарий', max_length=120)

    def __str__(self):
        return self.comment

    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'комментарии'
