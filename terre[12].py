#---- Affiche des valeurs du milieu---13


nombre_1 = input("Veuillez entrer un nombre :")
nombre_2 = input("Veuillez entrer un nombre :")
nombre_3 = input("Veuillez entrer un nombre :")


def nombre_valide(nbr_1, nbr_2, nbr_3):   
    if int(nbr_2) == int(nbr_1) == int(nbr_3):
        print("ERREUR : Veuillez entrez des nombres différents.")
    elif int(nbr_2) < int(nbr_1) < int(nbr_3):
        print(int(nbr_1))
    elif  int(nbr_3) < int(nbr_2) < int(nbr_1):
        print(int(nbr_2))
    elif int(nbr_1) < int(nbr_3) < int(nbr_2):
        print(int(nbr_3))
    elif int(nbr_1) < int(nbr_2) < int(nbr_3):
        print(int(nbr_2))
    elif int(nbr_1) > int(nbr_2) < int(nbr_3):
        print(int(nbr_3))
    elif int(nbr_1) < int(nbr_2) > int(nbr_3):
        print(int(nbr_1))

nombre_valide(nombre_1, nombre_2, nombre_3)