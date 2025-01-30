from random import randint

def select_randon_data(data_list):
    number_randon = randint(0, len(data_list)-1)
    return data_list[number_randon]

