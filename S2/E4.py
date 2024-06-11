# Exercice 4 - Reverse a list

# Method 1
tableau = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

tableau.reverse()
print(tableau)

# Method 2
tableau = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
longueur = len(tableau) - 1
tableau_inverse = []

while longueur >= 0:
    tableau_inverse.append(tableau[longueur])
    longueur -= 1
print(tableau_inverse)
