from Graph import Graph
from PiocheCarteDestination import PiocheCarteDestination
from PiocheCartesWagon import PiocheCartesWagon

class PlateauDeJeu(object):
    """ Classe representant le plateau du jeu des aventuriers du rail """
    def __init__(self, joueur1, joueur2):
        """
        initialise le plateau de jeu et ses 2 joueur, dont les attribut sont:
        :self.graph: initialise un graph pour le faire correspondre a la map du plateau
        :self.carte_wagon_visibles: initialise les carte wagon face visible
        :self.pioche_carte_wagon: init la pile de carte wagon a piocher
        :self.pioche_carte_destination: init la pile de carte destination
        :self.joueur1: j1 passer en argument passe en attribut du plateau
        :self.joueur2: pareil que pour j1
        """
        self.map = Graph()
        self.map.open_graph()
        self.construction = Graph()
        self.construction.nodes = self.map.nodes
        self.construction_possible = []
        self.cartes_wagon_visibles = []
        self.pioche_carte_wagon = PiocheCartesWagon()
        self.pioche_carte_destination = PiocheCarteDestination()
        self.joueur1 = joueur1
        self.joueur2 = joueur2

        #def des attributs aux joueurs
        self.joueur1.plateau_de_jeu = self
        self.joueur2.plateau_de_jeu = self
        self.joueur1.adversaire = joueur2
        self.joueur2.adversaire = joueur1

        # On ajoute les cartes wagons visibles
        for dummy_i in range(5):
            self.cartes_wagon_visibles.append(self.pioche_carte_wagon.piocher())

        # On fait la liste des constructions de route possible
        for edge in self.map.edges:
            self.construction_possible.append((edge[0], edge[1]))

    def finir_partie(self):
        """ Fini la partie, calcule le score du gagnant et l'affiche """
        score_joueur_1 = self.joueur1.calculer_score_finale()
        score_joueur_2 = self.joueur2.calculer_score_finale()

        if score_joueur_1 > score_joueur_2:
            print("Le joueur 1 a gagne la partie !!! :)")
        elif score_joueur_1 < score_joueur_2:
            print("Le joueur 2 a gagne la partie !!! :)")
        else:
            print("Vous etes arrive a egalite !!!!")

    def piocher_cartes_wagon(self, indice_1, indice_2):

        carte_1 = self.cartes_wagon_visibles.pop(indice_1)
        carte_2 = self.cartes_wagon_visibles.pop(indice_2 - 1)

        self.cartes_wagon_visibles.append(self.pioche_carte_wagon.piocher())
        self.cartes_wagon_visibles.append(self.pioche_carte_wagon.piocher())

        return carte_1, carte_2


    def jouer(self):
        """ Lance la partie de jeu """

        #Les joueurs piochent 4 cartes wagons et 3 cartes destinations
        for dummy_i in range(4):
            self.joueur1.cartes_wagons.append(self.pioche_carte_wagon.piocher())
            self.joueur2.cartes_wagons.append(self.pioche_carte_wagon.piocher())

        for dummy_i in range(3):
            self.joueur1.cartes_destinations.append(self.pioche_carte_destination.piocher())
            self.joueur2.cartes_destinations.append(self.pioche_carte_destination.piocher())

        #On lance le tour du premier joueur
        self.joueur1.jouer()
