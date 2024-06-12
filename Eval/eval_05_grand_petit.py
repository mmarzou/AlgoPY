# Exercice 5 - Le plus grand, le plus petit

tableau = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Valeurs du tableau : ", tableau)

# Trouver la plus grande et la plus petite valeur du tableau

# Initialisation des variables
plusGrand = tableau[0]
plusPetit = tableau[0]

# Parcourir le tableau
for i in range(1, len(tableau)):
    if tableau[i] > plusGrand:
        plusGrand = tableau[i]
    if tableau[i] < plusPetit:
        plusPetit = tableau[i]
print("La plus grande valeur du tableau est : ", plusGrand)
print("La plus petite valeur du tableau est : ", plusPetit)

# Pseudo code :

# Remplir le tableau avec 10 valeurs
# 
# Initialiser une variable plusGrand à la première valeur du tableau
# Initialiser une variable plusPetit à la première valeur du tableau
#
# Pour chaque valeur dans le tableau :
#     Si la valeur est plus grande que plusGrand :
#         Mettre à jour plusGrand
#     Si la valeur est plus petite que plusPetit :
#         Mettre à jour plusPetit
# 
# Afficher la plus grande valeur
# Afficher la plus petite valeur