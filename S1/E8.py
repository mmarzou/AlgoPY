# Exercice #8 - Délais de livraison

# Saisie d'une quantité de produit.
get_product_quantity = int(input("Entrez la quantité de produit: "))
print("La quantité de produit est de ", get_product_quantity)

# Choix du mode de livraison : rapide ou standard.
get_delivery_mode = str(input("Entrez le mode de livraison (rapide ou standard): "))
print("Le mode de livraison est ", get_delivery_mode)

# Si le mode de livraison est rapide.
if get_delivery_mode == "rapide":
    if get_product_quantity < 50:
        deliveryDate = "2 jours"
    elif get_product_quantity < 100:
        deliveryDate = "3 jours"
    else: 
        deliveryDate = "5 jours"
# Si le mode de livraison est standard.
else:
    if get_product_quantity < 50:
        deliveryDate = "4 jours"
    elif get_product_quantity < 100:
        deliveryDate = "5 jours"
    else:
        deliveryDate = "7 jours"
# Afficher le délai de livraison.
print("Le délai de livraison est de ", deliveryDate)