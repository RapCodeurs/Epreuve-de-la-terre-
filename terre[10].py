#---- NOMBRES PREMIERS --------11

nombre = input("Veuillez entrer un nombre :")

try:

    nombre = int(nombre)
    n = 2
    while n < nombre and nombre % n != 0:

        n = n + 1

    if n == nombre:
        print("Oui", nombre, "est un nombre premier.")
        
    else:
        print("Non", nombre, "n'est pas un nombre premier.")
        
except ValueError:
    print("ERREUR : Veuillez entrer un nombre entier.")