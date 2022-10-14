ETOILE = "*"
ESPACE = " "

def verif(type, nmb_ligne):
    if type == 1:
        return type1(nmb_ligne)
    elif type == 2:
        return type2(nmb_ligne)
    elif type == 3:
        return type3(nmb_ligne)
    elif type == 4:
        return type4(nmb_ligne)
    else:
        return print("Erreur")


def type1(nmb_ligne):
    for i in range(nmb_ligne):
        print(ETOILE*(i+1))

def type2(nmb_ligne):
    for i in range(nmb_ligne, -1, -1):
        print(ETOILE*i)

def type3(nmb_ligne):
    for i in range(nmb_ligne):
        print(ESPACE*(nmb_ligne-i),ETOILE*(i+1))

def type4(nmb_ligne):
    for i in range(nmb_ligne, -1, -1):
        print(ESPACE*(nmb_ligne-i),ETOILE*i)

def main():
    type = int(input("Entrez le type (1,2,3,4) : "))
    nmb_ligne = int(input("Entrez le nombre de ligne : "))

    verif(type, nmb_ligne)

main()