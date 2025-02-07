from .models import DistroLinux, Pokemon, Jogador
from ninja import ModelSchema, Schema


class LinuxSchema(ModelSchema):
    class Meta:
        model = DistroLinux
        fields = ['nome','imagem']


class PokemonSchema(ModelSchema):
    class Meta:
        model = Pokemon
        fields = ['nome','imagem']

class JogadorSchema(ModelSchema):
    class Meta:
        model = Jogador
        fields = ['nome','pontuacao']

class UploadSchema(Schema):
    nome: str