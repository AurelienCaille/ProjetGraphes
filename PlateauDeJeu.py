from Graphe import Graphe
from PiocheCarteDestination import PiocheCarteDestination
from PiocheCartesWagon import PiocheCartesWagon
from Joueur import Joueur

class PlateauDeJeu:
    """ Classe representant le plateau du jeu des aventuriers du rail """
    def __init__(self, joueur1, joueur2):

        self.graphe = Graphe()
        self.cartes_wagon_visibles = []
        self.pioche_carte_wagon = PiocheCartesWagon()
        self.pioche_carte_destination = PiocheCarteDestination()

        self.joueur1 = joueur1
        self.joueur2 = joueur2

    def jouer(self):

        self.joueur1.jouer()

        
