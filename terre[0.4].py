#--- Vérifier les nombres paires et impairs---- 5

nombre = input("Veuillez entrer un nombre : ")

try:

    if int(nombre) % 2 == 0:
        print("Paire")
    
    else:
        print("Impaire")
    nombre_str = int(nombre)
    
except ValueError:

    print("ERREUR : ")
    print("Tu ne me la maitras pas en l'envers !")  
