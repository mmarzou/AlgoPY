# Exercice 6 - Calcul d’une facture selon le nombre de photocopies effectuées (calculs par paliers). 
nCopy = int(input("Saisir le nombre de photocopies effectuées : "))

if nCopy <= 10:
    price = nCopy * 0.10
elif nCopy <= 20:
    price = 10 * 0.10 + (nCopy - 10) * 0.08
elif nCopy <= 50:
    price = 10 * 0.10 + 10 * 0.08 + (nCopy - 20) * 0.06
else:
    price = 10 * 0.10 + 10 * 0.08 + 30 * 0.06 + (nCopy - 50) * 0.03

# Calcule du prix de la facture
priceFacture = price + (price * 0.05)

print ("Le montant de la facture est de : ", price, " euros")