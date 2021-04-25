from django.db.models.signals import post_save
from django.dispatch import receiver # импортируем нужный декоратор
from django.core.mail import mail_managers
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from accounts.models import Profile
from .models import Post, Comment


@receiver(post_save, sender=Post)
def comment_created(sender, instance, created, **kwargs):
    if created:
        owner_email = User.objects.get(id__owner_id=instance).email

    msg = EmailMultiAlternatives(
        subject='Появились обновления в категории на которую вы подписаны',
        from_email='eugen.eisner@gmail.com',
        to='kaban80@gmail.com',
    )
    content = render_to_string('board/create_email.html', {
        'comment': owner_email,
    }
                               )
    msg.attach_alternative(content, "text/html")  # добавляем html
    msg.send()  # отсылаем

