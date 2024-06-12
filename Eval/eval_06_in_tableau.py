# Exercice 5 - Le plus grand, le plus petit

# 4 est présent deux fois dans le tableau
tableau = [1, 2, 3, 4, 5, 6, 7, 8, 9, 4]
print("Valeurs du tableau : ", tableau)

# Faire saisir un entier à l'utilisateur
nbrInput = int(input("Entrez un nombre entier : "))
print("Vous avez saisi : ", nbrInput)

# Rechercher si le nombre saisi est dans le tableau et si oui combien de fois
nbrOccurence = 0
for i in range(len(tableau)):
    if tableau[i] == nbrInput:
        nbrOccurence += 1
print("Le nombre saisi est présent ", nbrOccurence, " fois dans le tableau")

# Pseudo code :

# Remplir le tableau avec 10 valeurs
#
# Faire saisir un entier à l'utilisateur
#
# Initialiser un compteur à 0
#
# Pour chaque valeur dans le tableau :
#     Si la valeur est égale au nombre saisi :
#         Incrémenter le compteur
#
# Afficher le nombre de fois que le nombre saisi est présent dans le tableau