#-----FORMAT HEURE-------12
# J'ai eu des difficultés


"""
try:
        
    heure = int(input("entrer une heure: "))
    minut = int(input("entrer une heure: "))
    heure_PM = heure - 12
    heure_AM = heure + 12

    if heure:
        print(heure_PM,":",minut,"PM")
        
except ValueError:
    print("Veuillez entrez un nombre")"""

try:
        
    heure = int(input("entrer une heure: "))
    minut = int(input("entrer une heure: "))
    heure_AM = heure + 12

    if heure:
        print(heure_AM,":",minut,"AM")
        
except ValueError:
    print("Veuillez entrez un nombre")
 
