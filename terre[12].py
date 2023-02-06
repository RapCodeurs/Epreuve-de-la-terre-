#---- Affiche des valeurs du milieu---13

nombre_1 = input("Veuillez entrer un nombre :")
nombre_2 = input("Veuillez entrer un nombre :")
nombre_3 = input("Veuillez entrer un nombre :")

if int(nombre_2) == int(nombre_1) == int(nombre_3):
    print("ERREUR : Veuillez entrez des nombres différents.")

elif int(nombre_2) < int(nombre_1) < int(nombre_3):
    print(int(nombre_1))
elif  int(nombre_3) < int(nombre_2) < int(nombre_1):
    print(int(nombre_2))
elif int(nombre_1) < int(nombre_3) < int(nombre_2):
    print(int(nombre_3))
elif int(nombre_1) < int(nombre_2) < int(nombre_3):
    print(int(nombre_2))
elif int(nombre_1) > int(nombre_2) < int(nombre_3):
    print(int(nombre_3))
elif int(nombre_1) < int(nombre_2) > int(nombre_3):
    print(int(nombre_1))