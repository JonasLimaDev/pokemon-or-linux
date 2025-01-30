from random import randint

def select_randon_data(data_list):
    number_randon = randint(0, len(data_list)-1)
    return data_list[number_randon]

def save_player(data_to_save):
    jogador = Jogador.objects.create(**data_to_save)
    return jogador
