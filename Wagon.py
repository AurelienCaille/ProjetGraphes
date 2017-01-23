class Wagon:
    couleurs = ["Bleu", "Rose", "Orange", "Blanc", "Vert", "Jaune", "Noir", "Rouge", "Multicolore"]
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
