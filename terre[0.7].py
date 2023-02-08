#----- Taille d'une chaine ------------8


h = ("bonjour")

try:
    h_int = str(h)
    if h=="":
        print("ERREUR.")
    elif len(h) > 10:
        print("ERREUR.")
    else:
        print(len(h))
except TypeError:
    print("ERREUR.")

