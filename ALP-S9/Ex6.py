NOTES = [3, 6, 5.5, 4.5, 2.5, 4, 5, 4, 3, 4, 2.5, 4.5, 5, 5, 4, 3]


def moyenne(notes):
    total = sum(notes)
    return round(total/len(notes), 1)


def notes_inf(notes):
    return len([note for note in notes if note < 4])


def meilleure_note(notes):
    return max(notes)


def indice_meilleure_note(notes):
    return notes.index(meilleure_note(notes))


print("Moyenne : ", moyenne(NOTES))
print("Nombre de notes inférieures à la moyenne : ", notes_inf(NOTES))
print("Meilleure note : ", meilleure_note(NOTES))
print("Indice de la meilleure note : ", indice_meilleure_note(NOTES))
