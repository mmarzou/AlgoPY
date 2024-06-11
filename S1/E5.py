# Conso client habituelle en minutes
conso = float(input("Saisir la consommation mensuelle en minutes : "))
print ("La consommation mensuelle est de : ", conso, " minutes")
# Offre mobile n°1 :
fixedOffer1 = 10
variableCost1 = 0.05

offer1 = fixedOffer1 + (conso * variableCost1)
# print ("Le montant de l'offre mobile n°1 est de : ", offer1)

# Offre mobile n°2 :
fixedOffer2 = 20
variableCost2 = 0.02

offer2 = fixedOffer2 + (conso * variableCost2)
# print ("Le montant de l'offre mobile n°2 est de : ", offer2)

# Suggestion de l'offre la plus avantageuse
if offer1 < offer2:
    print ("L'offre la plus avantageuse est l'offre mobile n°1")
else: print ("L'offre la plus avantageuse est l'offre mobile n°2")