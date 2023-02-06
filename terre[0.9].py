#-----Racines carrés d'un nombre-----10

nombre = input("Veuillez entrer un nombre :")

try:

    carre = int(nombre)**2
    if int(nombre) < 0:
        print("ERREUR : Veuillez entrer un nombre positif !")
    else:
        print(carre)
except ValueError:
    print("ERREUR : Veuillez entrer un nombre !")

    