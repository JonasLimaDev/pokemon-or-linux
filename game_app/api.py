from ninja import NinjaAPI, Schema
from typing import List
from .services import select_randon_data
from .schemas import PokemonSchema, LinuxSchema, JogadorSchema
from .models import Pokemon, DistroLinux, Jogador

api = NinjaAPI()


@api.get('/pokemon/{pokemon_name}', response=PokemonSchema)
def buscar_pokemon(request, pokemon_name: str):
    pokemon = get_object_or_404(Pokemon,nome=pokemon_name)
    return pokemon


@api.get('/linux/{linux_name}', response=LinuxSchema)
def buscar_linux(request, linux_name: str):
    linux = get_object_or_404(Dis,nome=linux_name)
    return linux


@api.get('/sorteia_nome')
def buscar_nome_sorteado(request):
    pokemons = Pokemon.objects.all()
    distros = DistroLinux.objects.all()
    positional_data = randint(0,6)
    if positional_data % 2 == 0:
        selected_distro  = select_randon_data(distros)
        return {'name': selected_distro.nome}
    else:
        selected_pokemon = select_randon_data(pokemons)
        return {'name': selected_pokemon.nome}


@api.get('/verificar')
def verificar_nome(request, nome_search: str or None):
    if Pokemon.objects.filter(nome=nome_search):
        return {'resultado': 'Pokemon'}
    elif DistroLinux.objects.filter(nome=nome_search):
        return {'resultado': 'Distribuição Linux'}
    else:
        return {'resultado': 'Não Localizado'}


@api.post('/jogador', response=JogadorSchema)
def salvar_jogador(request, payload: JogadorSchema):
    jogador = Jogador.objects.create(**payload.dict())
    return jogador


@api.get('/jogadores', response=List[JogadorSchema])
def buscar_jogadores(request):
    jogadores = Jogador.objects.all()
    return jogadores