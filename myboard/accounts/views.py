# from django.contrib.auth import authenticate, login
# from django.http import HttpResponse
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DeleteView
from django.contrib.auth.models import User

from .forms import RegisterForm
from .models import Profile
from board.models import Post, Comment
from .forms import LoginForm
from .filters import PostFilter


class UserLoginView(LoginView):
    template_name = 'registration/login.html'
    form_class = LoginForm
    next_page = '/accounts/profile/'


class UserLogOutView(LogoutView):
    template_name = 'registration/logout.html'
    next_page = '/'


# функция регистрации пользователя
def register(request):
    if request.method == 'POST':
        # получаем данные формы
        form = RegisterForm(request.POST)
        # проверяем
        if form.is_valid():
            new_user = form.save(commit=False)
            # когда мы вызовем new_user.save().
            new_user.save()
            Profile.objects.create(user=new_user,
                                   email=new_user.email,
                                   first_name=new_user.first_name,
                                   last_name=new_user.last_name,
                                   )
            # добавляю профиль
            # если все хорошо перекидываю юзера на страницу registration_complete.html
            return render(request, 'accounts/registration_complete.html',
                          {'new_user': new_user})
    else:
        form = RegisterForm()

    return render(request, 'accounts/register.html', {'form': form})


class UserProfile(LoginRequiredMixin, ListView):
    model = Profile
    template_name = 'accounts/profile.html'
    context_object_name = 'profil'
    # queryset = Comment.objects.all()

    def get_context_data(self, **kwargs):
        id = self.kwargs.get('pk')
        context = super().get_context_data(**kwargs)
        # добавляю в контекст только посты определенного пользователя
        context['posts'] = Post.objects.filter(owner=self.request.user)
        context['comments'] = Comment.objects.filter(post_id=id)
        return context





