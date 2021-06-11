from django.urls import path
from . import views


urlpatterns = [
    path('music/', views.SongList.as_view()),
    path('music/<int:pk>/', views.song_detail.as_view()),
]