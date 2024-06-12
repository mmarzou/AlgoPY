print("Bubble Sorting")

# Tableau à trier
tableau = [5, 3, 8, 6, 7, 2, 4, 1, 9, 34]

# Affichage du tableau avant le tri
print("Tableau avant le tri : ", tableau)

# Tri à bulle
for i in range(0, len(tableau)):
    for j in range(i+1, len(tableau)):
        if tableau[i] >= tableau[j]:
            tableau[i], tableau[j] = tableau[j], tableau[i]
print("Tableau après le tri : ", tableau)

# Pseudo code :

# Initialiser un tableau de 10 valeurs
#
# Afficher le tableau avant le tri
#
# Pour chaque valeur dans le tableau à partir de la première valeur :
#     Pour chaque valeur dans le tableau à partir de la valeur suivante :
#         Si la valeur courante est supérieure à la valeur suivante :
#             Echanger les valeurs
#
# Afficher le tableau après le tri