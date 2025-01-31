from random import randint


def select_randon_data(data_list):
    try:
        number_randon = randint(0, len(data_list)-1)
    except:
        number_randon = 0
    return data_list[number_randon]
