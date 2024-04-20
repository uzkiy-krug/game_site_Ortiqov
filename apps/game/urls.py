from django.urls import path
from .views import GameListView

app_name = 'game'

urlpatterns = [
    path('gamelist/', GameListView.as_view(), name='game-list'),
]