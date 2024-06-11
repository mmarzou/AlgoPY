# Exerice 1 : Algorithme qui permet d'afficher le contenu d'un tableau déjà rempli de 5 entiers du dernier au premier élément.

print("Affichage du contenu d'un tableau de 5 entiers du dernier au premier élément")
tableau = [0, 1, 2, 3, 4]
print("dans l'ordre :")

for i in range(0, 5, 1):
    print(tableau[i])
print("dans l'ordre inverse :")
for i in range(4, -1, -1):
    print(tableau[i])
print("Affichage du contenu d'un tableau de 5 entiers du premier au dernier élément")