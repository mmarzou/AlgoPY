# Exercice 2 - Elections

# Faîtes saisir le pourcentage (type réel) des voix obtenues par un candidat.
voicePercentage = float(input("Entrez le pourcentage des voix obtenues par un candidat : "))

# Afficher son satut selon les trois règles suivantes :
if voicePercentage < 5:
    print("Le candidat est éliminé")
elif voicePercentage < 50:
    print("Le candidat est qualifié pour le second tour")
else:
    print("Le candidat est élu")
print("Fin du programme")

# Pseudo code :

# Faire saisir le pourcentage des voix obtenues par un candidat
# Si le pourcentage est inférieur à 5 :
#     Afficher que le candidat est éliminé
# Sinon si le pourcentage est inférieur à 50 :
#     Afficher que le candidat est qualifié pour le second tour
# Sinon :
#     Afficher que le candidat est élu
# Fin du programme