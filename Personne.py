# Class Personne
class Personne:
    nom = ""
    prenom = ""
    age = 0

    # initialisateur
    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = age  

    # méthode afficher
    def afficher(self):
        print("{}, {}, {}".format(self.nom, self.prenom, self.age))

    # méthode viellir
    def viellier(self):
        self.age += 1
