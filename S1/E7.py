# Augmention des tarifs :

# Saisie d'un prix unitaire de produit
priceUnit = float(input("Saisir le prix unitaire du produit : "))

if priceUnit < 20:
    price = priceUnit + (priceUnit * 0.1)
elif priceUnit < 50:
    price = priceUnit + (priceUnit * 0.075)
elif priceUnit < 100:
    price = priceUnit + (priceUnit * 0.05)
else: 
    price = priceUnit + (priceUnit * 0.025)

print("Le prix du produit est : ", price)