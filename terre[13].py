#----- Trié ou pas --------14
# pas terminé

liste = []
for i in range(6):
    nbr = input()
    liste.append(int(nbr))


if int(liste) == sorted(liste):
    print(liste)
    print("Triée !")

else:
    print(liste)
    print("Pas triée !")

