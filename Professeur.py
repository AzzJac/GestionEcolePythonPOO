# class Professeur
from Personne import *

class Professeur(Personne):
    salaire = 0

    # initialisateur
    def __init__(self, nom, prenom, age, salaire):
        # appel l'init du parent
        super().__init__(nom, prenom, age)
        # init le salaire
        self.salaire = salaire

    # réécrit la méthode afficher
    def afficher(self):
        # appel la méthode du parent
        super().afficher()
        # affiche en plus le salaire
        print("Salaire : {}".format(self.salaire))

    # méthode caluler_cout
    def caluler_cout(self):
        return self.salaire * 12