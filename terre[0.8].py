#----- les puissances -------- 9

nombre = input("Veuillez entrer un nombre :")
exposant = input("Veuillez entrer un exposant :")

try:
    resultat = int(nombre)**int(exposant)
    if int(exposant) < 0:
        print("ERREUR : Vous devez entrer un nombre positif.")
    else:
        print(resultat)
    
except ValueError:
    print("ERREUR : Vous devez entrer un nombre.")