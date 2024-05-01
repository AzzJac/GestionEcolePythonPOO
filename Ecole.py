class Ecole:

    nom = ""
    adresse = ""
    budget = 0

    def __init__(self, nom, adresse, budget):
        self.nom = nom
        self.adresse = adresse
        self.budget = budget
        # liste de professeurs et d'élèves
        self.professeurs = []
        self.eleves = []
    
    def ajouter_professeur(self, professeur):
        self.professeurs.append(professeur)
    
    def ajouter_eleve(self, eleve):
        self.eleves.append(eleve)

    def afficher(self):
        print("{}, {}, {}".format(self.nom, self.adresse, self.budget))
        # affiche les professeurs
        print("--- Professeurs ---")
        for professeur in self.professeurs:
            professeur.afficher()

        # affiche les élèves
        print("--- Elèves ---")
        for eleve in self.eleves:
            eleve.afficher()
