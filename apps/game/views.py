from django.shortcuts import render
from django.views.generic import TemplateView


class GameListView(TemplateView):
    template_name = 'game/games.html'