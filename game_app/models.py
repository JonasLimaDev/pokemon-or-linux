from django.db import models

# Create your models here.
class DistroLinux(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False, unique=True)
    imagem = models.ImageField(null=False, blank=False)

    def __str__(self):
        return self.nome


class Pokemon(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False, unique=True)
    imagem = models.ImageField(null=False, blank=False)

    def __str__(self):
        return self.nome


class Jogador(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False, unique=True)
    pontuacao = models.IntegerField( null=False, blank=False)

    def __str__(self):
        return self.nome
