from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Pokemon, DistroLinux
# Create your views here.

# class PokemonsListView(ListView):
#     model = Pokemon
#     template_name = 'app/lista_pokemons.html'

class GameView(TemplateView):
    template_name = 'game_app/game.html'


class TopJogadoresView(TemplateView):
    template_name = 'game_app/top_jogadores.html'
# def listar_pokemons(request):
#     return render(request, 'app/lista_pokemons.html')