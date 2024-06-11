print ("Saisir la quantité de produit")
# Saisie d'une quantité
qProduct = float(input("Veuillez saisir une quantité de produit :"))
print ("Quantité entrée :", qProduct)
# Saisie d'un prix HT
pHT = float(input("Veuillez saisir un prix unitaire Hors-taxe :"))
# Calculer le montant total HT
total = qProduct * pHT
print ("Le montant total est : ", qProduct * pHT)

# Appliquer une remise...
if pHT < 200:
    tRemise = 2.5
elif pHT < 400:
    tRemise = 5
elif pHT < 700:
    tRemise = 7.5
else: tRemise = 10

print ("Le taux de remise est de : ", tRemise)
# Calculer le montant de la remise
remise = total * (tRemise / 100)
print ("Le montant de la remise est : ", remise)
# Calculer le montant total TTC
ttc = total - remise
print ("Le montant total TTC est : ", ttc)
# Calculer le montant de la TVA
tva = ttc * 0.2
print ("Le montant de la TVA est : ", tva)
