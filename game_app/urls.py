from django.urls import path
from .api import api
from .views import GameView
# from .views import PokemonsListView, game


urlpatterns = [
    path('api/', api.urls),
    path('partida/', GameView.as_view(), name='game_page')
]