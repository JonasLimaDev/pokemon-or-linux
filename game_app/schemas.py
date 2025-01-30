from .models import DistroLinux, Pokemon
from ninja import ModelSchema


class LinuxSchema(ModelSchema):
    class Meta:
        model = DistroLinux
        fields = ['nome','imagem']


class PokemonSchema(ModelSchema):
    class Meta:
        model = Pokemon
        fields = ['nome','imagem']