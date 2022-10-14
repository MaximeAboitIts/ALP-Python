def affichage(nomberMax):
    for i in range(nomberMax, -1, -1):
        if i % 2 == 0:
            print(i)

def main():
    nomberMax = int(input("Entrez un nombre maximum : "))
    affichage(nomberMax)

main()