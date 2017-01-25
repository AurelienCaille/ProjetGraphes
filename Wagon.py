couleurs = ["Bleu", "Rose", "Orange", "Blanc", "Vert", "Jaune", "Noir", "Rouge", "Multicolore"]
class Wagon:
    def __init__(self, couleur):
        """
        :attribut self.couleur: la couleur passe en parametre defini la couleur du wagon
        """
        self.couleur = couleur


    def __repr__(self):
        """
        renvoie letat de la couleur du wagon
        """
        return "Wagon: " + self.couleur

    def __eq__(self, other):
        return self.couleur == other.couleur
