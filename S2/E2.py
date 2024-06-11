# Exerice 2 : Algorithme qui permet de saisir 10 entiers, et qui les range au fur et à mesure dans un tableau.

tableau = []

for i in range(0, 10):
    tableau.append(int(input("Entrez un nombre : ")))
    print (tableau[i])
print(tableau)