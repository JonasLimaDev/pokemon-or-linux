from django.urls import path
from .api import api
# from .views import PokemonsListView, game


urlpatterns = [
    path('api/', api.urls),
]