from django import forms
from django.contrib.auth.models import User

from allauth.account.forms import SignupForm, LoginForm

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


# Создаём форму LoginForm для входа в кабинет
class LoginForm(LoginForm):
    class Meta:
        model = User
        fields = ('username', 'password')


# регистрация пользователя, переопределяю форму allauth
class SignupForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


