from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from .models import Profile
from board.models import Post, Comment


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





