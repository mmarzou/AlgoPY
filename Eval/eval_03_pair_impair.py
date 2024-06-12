# Exercice 3 - Pair ou impair

# Remplir un tableau de 10 entiers
tableau = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Afficher le tableau
print("Tableau : ", tableau)

# Parcourir le tableau
print("Tableau for loop :")
for i in range(len(tableau)):
    if tableau[i] % 2 == 0:
        print(tableau[i], " est pair")
    else:
        print(tableau[i], " est impair")
print("Fin de la boucle for loop\n")

### Pseudo code : for loop ###

# Rempli le tableau avec 10 entiers
# Pour chaque nombre dans le tableau :
#    Si le nombre est pair :
#        Afficher le nombre et qu'il est pair
#    Sinon :
#        Afficher le nombre et qu'il est impair
# Fin de la boucle for loop

i = 0
print("Tableau while loop :")
while i < len(tableau):
    if tableau[i] % 2 == 0:
        print(tableau[i], " est pair")
    else:
        print(tableau[i], " est impair")
    i += 1
print("Fin de la boucle while loop\n")

### Pseudo code : while loop ###
# Réinisialiser l'index à 0
# Tant que l'index est inférieur à la taille du tableau :
#    Si le nombre à l'index est pair :
#        Afficher le nombre et qu'il est pair
#    Sinon :
#        Afficher le nombre et qu'il est impair
#    Incrémenter l'index
# Fin de la boucle while loop