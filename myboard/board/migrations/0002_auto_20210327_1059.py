# Generated by Django 3.1.7 on 2021-03-27 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='board',
            name='is_active',
        ),
        migrations.AddField(
            model_name='comment',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='принято'),
        ),
    ]
