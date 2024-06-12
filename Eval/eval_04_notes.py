# Exercice 4 - Calcul de la moyenne

notes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

count = 0

# Afficher le tableau
print("Tableau : ", notes)

if len(notes) > 0:
    for i in range(len(notes)):
        count += notes[i]
    moyenne = count / len(notes)
    print("La moyenne de ces notes est : ", moyenne)
print("Fin du programme")

# Pseudo code :

# Remplir le tableau avec 10 notes
# Initialiser un compteur à 0
# Si le tableau n'est pas vide :
#     Pour chaque note dans le tableau :
#         Ajouter la note au compteur
#     Calculer la moyenne
#     Afficher la moyenne
# Fin du programme