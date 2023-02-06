#-- Divisions----- 6

dividende = input("Veuillez entrer un nombre : ")
diviseur = input("Veuillez entrer un nombre : ")


try:
    resultat = int(dividende)//int(diviseur)
    reste =  int(dividende)%int(diviseur)

    if int(dividende) < int(diviseur):
        print("ERREUR")
    else:
        print("résultat : ", resultat)
        print("reste : ", reste)

except ZeroDivisionError and ValueError:
    print("ERREUR")
