from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class platform(TemplateView):
    template_name = 'third_task/platform.html'


class games(TemplateView):
    template_name = 'third_task/games.html'
    games = ['Atomic Heart', 'Cyberpunk 2077', 'PayDay 2']
    extra_context = {
        'games': games
    }


class cart(TemplateView):
    template_name = 'third_task/cart.html'
