# Class Eleve
from Personne import *

class Eleve(Personne):

    # initialisateur
    def __init__(self, nom, prenom, age):
        # appel l'init du parent
        super().__init__(nom, prenom, age)
        # init la liste de moyennes
        self.moyennes = []

    # réécrit la méthode afficher
    def afficher(self):
        # appel la méthode du parent
        super().afficher()
        # affiche en plus la liste de moyennes
        print("Moyennes : {}".format(self.moyennes))

    # méthode ajouter_moyenne
    def ajouter_moyenne(self, moyenne):
        # ajoute à la liste la moyenne
        self.moyennes.append(moyenne)

    # moyenne_gen
    def moyenne_gen(self):
        return sum(self.moyennes) / len(self.moyennes)