L10_INT = [-3, -1, 0, 1, 1, 4, 6, -1, 7, 8] #liste de 10 nombres entiers

L2_STR = ["alice", "bob"] #liste de deux chaînes de caractères 

L1_FLO = [-3.5] #liste de un seul nombre réel 

L0 = [] #liste vide

def afficher_liste_positif(ma_liste):
    for i in ma_liste:
        if i > 0:
            print(i)

afficher_liste_positif(L10_INT)