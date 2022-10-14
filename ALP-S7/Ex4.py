def affichage(n):
    for i in range(0, n):
        n += i
    print(n)

def main():
    nmb_choisis = int(input("Entrez un nombre : "))

    affichage(nmb_choisis)

main()