class CarteWagon:
    def __init__(self, couleur):
        """
        :attribut self.couleur: def la couleur de la carte wagon passee en parametre en tant qu attribut 
        """
        self.couleur = couleur


    def __repr__(self):
        """
        renvoie l'etat de la couleur de la carte wagon
        """
        return "Carte Wagon de couleur: " + self.couleur
