from django_filters import FilterSet, ModelChoiceFilter, ChoiceFilter

from board.models import Post, Comment
from django import forms


class PostFilter(FilterSet):
    # фильтрую только те объявления которые принадлежат пользователю вошедшему в систему
#    post = ModelChoiceFilter(queryset=Comment.objects.filter(post_id=True).values('name'),
#                             widget=forms.Select(attrs={
#                                 'class': 'form-control mb-2',
#                             })),

    class Meta:
        model = Comment
        fields = ['post']
    # фильтрую первичный набор запросов по request объект,
    # переопределяю FilterSet.qs. чтобы фильтровать только те комменты,
    # которые принадлежат постам пользователя вошедшему в систему.

    @property
    def qs(self):
        parent = super().qs
        owner = getattr(self.request, 'user', None)

        return parent.filter(id=True) \
                | parent.filter(post=owner)
