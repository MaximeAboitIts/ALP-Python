def affichage(nomberMax):
    for i in range(0, nomberMax+1):
        if i % 2 == 0:
            print(i)

def main():
    nomberMax = int(input("Entrez un nombre maximum : "))
    affichage(nomberMax)

main()