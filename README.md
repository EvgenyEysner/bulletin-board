# Bulletin Board
<h2>Команды</h2>
<hr>
<b>установка Django/ создание проекта</b>

1. <i>pip install django</i>
2. <i>django-admin startproject myboard</i>
>> cd myboard
3. <i>python manage.py startapp board</i>
<hr> 
<b>Git</b>

4. инициализируем проект: <i>git init</i>
5. создам файл .gitignore и заполняем его
> > пример: https://djangowaves.com/tips-tricks/gitignore-for-a-django-project/
6. файл с зависимостями: <i>pip freeze > requirements.txt</i>
7. делаем миграции: <i>python manage.py migrate</i>
8. создаем admin: <i>python manage.py createsuperuser
</i>
9. Запускаем проект: <i>python manage.py runserver</i>
10. Делаем первый commit/push Git
>> settings.py <br> 
import os <br>
BASE_DIR = os.path.dirname(os.path.dirname(__file__))<br>
INSTALLED_APPS [
<br> 'board.apps.BoardConfig',
<br>]
<br> меняю пути в TEMPLATES
'DIRS': [os.path.join(BASE_DIR, 'templates')],<br>
DB 'NAME' --> os.path.join(BASE_DIR, 'db.sqlite3')<br>
добавляю пути для статики:<br>
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)<br>
т.к. будут картинки добавляю директорию для Media<br>
MEDIA_URL = '/media/'<br>
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')<br>
>>
В главный urls.py добавлю 
>> from django.conf import settings<br>
from django.conf.urls.static import static
>> urlpatterns = [<br>
    path('admin/', admin.site.urls),<br>
    path('', include('board.urls')),<br>
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

для того чтобы все правильно работало + Pillow для работы с изображениями
<br>
<i>pip install pillow</i>