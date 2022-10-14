def main():
    nombre = int(input("Entrez un nombre pour avoir sa table de multiplication : "))
    print("Livret de", nombre)
    for i in range(12):
        print(f"{i + 1} x {nombre} = {(i + 1) * nombre}")

main()