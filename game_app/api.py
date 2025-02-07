from ninja import NinjaAPI, Schema, File
from ninja.files import UploadedFile
from typing import List
from .services import select_randon_data
from .schemas import PokemonSchema, LinuxSchema, JogadorSchema, UploadSchema
from .models import Pokemon, DistroLinux, Jogador
from random import randint
from django.shortcuts import get_object_or_404
from ninja.errors import HttpError

api = NinjaAPI()


@api.get('/pokemon/{pokemon_name}', response=PokemonSchema)
def buscar_pokemon(request, pokemon_name: str):
    pokemon = get_object_or_404(Pokemon,nome=pokemon_name)
    return pokemon


@api.post('/pokemon', response=PokemonSchema)
def salvar_pokemon(request, payload: UploadSchema, file: File[UploadedFile]):
    if Pokemon.objects.filter(nome=payload.nome) ==  []:
        pokemon = Pokemon.objects.create(nome = payload.nome,
        imagem = file)
        return pokemon
    else:
        raise HttpError(400, f"Name {payload.nome} already exists")


@api.get('/linux/{linux_name}', response=LinuxSchema)
def buscar_linux(request, linux_name: str):
    linux = get_object_or_404(DistroLinux,nome=linux_name)
    return linux


# @api.post('/distro', response=LinuxSchema)
# def salvar_distro(request, payload: DistroSchema):
#     distro = DistroLinux.objects.create(**payload.dict())
#     return distro


@api.get('/sorteia_nome')
def buscar_nome_sorteado(request):
    pokemons = Pokemon.objects.all()
    distros = DistroLinux.objects.all()
    positional_data = randint(0,1)
    if positional_data == 0:
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


@api.get('/top/jogadores', response=List[JogadorSchema])
def buscar_top_jogadores(request):
    jogadores = Jogador.objects.order_by("-pontuacao")[:10]
    return jogadores