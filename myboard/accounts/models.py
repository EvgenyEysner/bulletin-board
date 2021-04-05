from django.db import models
from django.contrib.auth.models import User


# расширяю базовою модель пользователя
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='ник')
    first_name = models.CharField('имя', max_length=120, blank=True, null=True)
    last_name = models.CharField('фамилия', max_length=240, blank=True, null=True)
    birthdate = models.DateField('день рождения', blank=True, null=True)
    avatar = models.ImageField('аватар', upload_to='avatars/%Y/%m/%d', blank=True)

    def __str__(self):
        return "Профиль пользователя %s" % self.user.username

    class Meta:
        verbose_name = 'профиль'
        verbose_name_plural = 'профили'

