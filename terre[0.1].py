#---Afficher son nom du fichier---- 2
"""
f = "Untitled-1.py"
print(f)
"""

import os 

repertoire = os.getcwd()
file = os.path.realpath(__file__)
print("C'est ça : ", file)