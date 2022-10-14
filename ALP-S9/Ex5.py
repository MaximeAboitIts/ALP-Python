RELEVES = [11.8, 14.4, 18.6, 16.5, 11.5, 12.3, 9.1]


def moyenne(releves):
    s = 0
    for temp in releves:
        s = s + temp
    m = s / len(releves)
    print("La température moyenne est : ", m)


moyenne(RELEVES)


def nb_temp_inf_15(releves):
    s = 0
    for temp in releves:
        if temp < 15:
            s = s + 1
    print("Le nombre de températures inférieures à 15 est : ", s)


nb_temp_inf_15(RELEVES)
