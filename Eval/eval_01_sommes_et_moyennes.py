# Exercice 1 - Sommes et moyennes

# Faire saisir trois nombre entier à l'utilisateur
int1, int2, int3 = input("Entrez trois nombre entier : ").split()
print("Vous avez saisi les nombres suivants : ", int1, int2, int3)

# Conversion des nombres saisis en entier
somme = int(int1) + int(int2) + int(int3)
# Calcul de la moyenne
moyenne = somme / 3
# Affichage de la somme et de la moyenne
print("La somme de ces trois nombres est : ", somme)
print("La moyenne de ces trois nombres est : ", moyenne)

# Pseudo code :

# Faire saisir trois nombre entier à l'utilisateur
# Convertir les nombres saisis en entier
# Calculer la somme des trois nombres
# Calculer la moyenne des trois nombres
# Afficher la somme et la moyenne