nomMaga = "PTIPRI"
noClient = int(input("Entrez un numéro de client: "))
firstArticle = int(input("Entrez le prix du premier article: "))
secondArticle = int(input("Entrez le prix du deuxième article: "))
rabais = 0

if (firstArticle < secondArticle):
    rabais = (firstArticle * 50 / 100)
elif (firstArticle > secondArticle):
    rabais = (secondArticle * 50 / 100)

prixFinal = firstArticle + secondArticle - rabais

print(nomMaga)
print("Achats effectués par le client n°", noClient)
print("Prix des 2 articles achetés :", firstArticle,
      "et", secondArticle, "==> Prix à payer:", prixFinal)
print("Merci pour votre achat.")
print("En cas de problème, vous pouvez nous les retourner dans les 7 jours.")
