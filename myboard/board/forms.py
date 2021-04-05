from django.forms import ModelForm, TextInput, EmailInput, Select, Textarea, MultiWidget, FileField
from .models import Comment, Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['category', 'name', 'description', 'image', 'content']

#        widgets = {
#            'category': Select(attrs={
#                'class': 'form-control',
#                'placeholder': 'Название статьи'
#            }),

#           'name': TextInput(attrs={
#                'class': 'form-control',
#                'placeholder': 'Введите текст...'
#            }),

#            'description': Textarea(attrs={
#               'class': 'form_control',
#                'placeholder': 'Добавить описание'

#           }),

#            'content': Textarea(attrs={
#                'class': 'form-control',
#            }),
#        }


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']

        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя'
            }),
            'email': EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'E-Mail'
            }),
            'body': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Комментарий'
            })

        }

