# Imports

# Constantes
argent = 0
# Procédures et fonctions
def fonction(oui,non, argent):
    if((oui + non) > 1000 and (oui + non) <= 2000):
        argent = argent + 8000
    elif((oui + non) > 2000):
        argent = argent + 12000
    else:
        argent = argent + 5000

    if(oui > non):
        argent = argent + 2000 

    if(100*oui/(oui+non) > 65):
        argent = argent + 4000
    
    print("Le montant pour cette commune ayant", oui, "OUI et", non, "NON sera de CHF", argent, ".-")

# Procédure main()
def main():
    vote_oui = int(input("Nombre de OUI: "))
    vote_non = int(input("Nombre de NON: "))
        
    fonction(vote_oui,vote_non, argent)
    
# Appel de la procédure main()
if __name__ == "__main__":
    main()