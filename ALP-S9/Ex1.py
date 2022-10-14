L10_INT = [-3, -1, 0, 1, 1, 4, 6, -1, 7, 8] #liste de 10 nombres entiers

L2_STR = ["alice", "bob"] #liste de deux chaînes de caractères 

L1_FLO = [-3.5] #liste de un seul nombre réel 

L0 = [] #liste vide

def premier_de_la_liste(liste):
    return liste[0]

def dernier_de_la_liste(liste):
    return liste[-1]

def avant_dernier_de_la_liste(liste):
    return liste[-2]

def nieme_valeur_de_la_liste(liste, n):
    return liste[n]

try:
    print(nieme_valeur_de_la_liste(L2_STR, 0))
except:
    print("ERROR")