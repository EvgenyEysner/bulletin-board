from django.urls import path
from . views import IndexView, AdView, AdCreateView, AdUpdateView, AdDeleteView


urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('<int:pk>/', AdView.as_view(), name='post'),
    path('add/', AdCreateView.as_view(), name='post_create'),
    path('<int:pk>/update/', AdUpdateView.as_view(), name='post_update'),
    path('<int:pk>/delete/', AdDeleteView.as_view(), name='post_delete'),
]