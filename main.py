from Professeur import *
from Eleve import *
from Ecole import *

# crée un professeur
nicolas = Professeur("Chevalier", "Nicolas", 48, 2000)
#nicolas.afficher()

# crée un élève
jacques = Eleve("Bourbonnais", "Jacques", 19)

# ajoute une moyenne
jacques.ajouter_moyenne(15)

# crée une école
ecole = Ecole("Epsi", "7 Rue Jean-Marie Leclair, 69009 Lyon", 1000000)

# ajoute le professeur
ecole.ajouter_professeur(nicolas)

# ajoute l'élève
ecole.ajouter_eleve(jacques)

ecole.afficher()
