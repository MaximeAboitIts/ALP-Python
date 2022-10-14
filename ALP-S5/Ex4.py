def main():
    nombre = int(input("Entrez un nombre pour avoir sa table de multiplication : "))
    nombre_max = int(input("Entrez le nombre maximum à afficher : "))
    print("Livret de", nombre)
    for i in range(nombre_max):
        print(f"{i + 1} x {nombre} = {(i + 1) * nombre}")

main()