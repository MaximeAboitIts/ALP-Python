number1 = int(input("Veuillez entrer un chiffre: "))
number2 = int(input("Veuillez entrer un chiffre: "))
number3 = int(input("Veuillez entrer un chiffre: "))

def checkNumber(n1,n2,n3):
    if(n1 < 0):
        print("Le nombre", n1, "est négatif")
    elif(n1 == 0):
        print("Le nombre", n1, "est nul")
    else:
        print("Le nombre", n1, "est positif")
    
    if(n2 < 0):
        print("Le nombre", n2, "est négatif")
    elif(n2 == 0):
        print("Le nombre", n2, "est nul")
    else:
        print("Le nombre", n2, "est positif")

    if(n3 < 0):
        print("Le nombre", n3, "est négatif")
    elif(n3 == 0):
        print("Le nombre", n3, "est nul")
    else:
        print("Le nombre", n3, "est positif")

checkNumber(number1, number2, number3)