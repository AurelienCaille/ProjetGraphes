
class Joueur(object):
    """Classe abstraite representant un joueur"""
    def __init__(self):
        """
        :self.adversaire: init le joueur adverse de Joueur
        :self.score: represente le score du Joueur, commance a 1
        :self.cartes_wagons: init la liste vide de cartes wagon du joueur
        :self.cartes_destinations: init la lst vide de carte destination
        :self.reserve_wagon: init le stock de wagon de couleur du joueur
        :self.plateau_de_jeu: init a None le plateau de jeu associe au joueur
        self.plateau_de_jeu sera defini par l objet de classe plateau_de_jeu
        """

        self.adversaire = None
        self.score = 0
        self.cartes_wagons = []
        self.cartes_destinations = []
        self.reserve_wagon = []
        self.plateau_de_jeu = None


    def calculer_score_finale(self):
        """ Calcule le score final du joueur selon les regles du jeu CF: ManuelDuJoueur"""
        pass


    def prendre_cartes_wagons(self, indice1, indice2):
        """
        Selectionne 2 des cartes wagons visibles
        et complete les cartes manquantes sur le plateau de jeu
        """

        #On ajoute les cartes a la mains
        self.cartes_wagons.append(self.plateau_de_jeu.cartes_wagon_visibles.pop(indice1))
        self.cartes_wagons.append(self.plateau_de_jeu.cartes_wagon_visibles.pop(indice2))

        #On revele deux nouvelles cartes
        self.plateau_de_jeu.cartes_wagon_visibles.append(\
            self.plateau_de_jeu.pioche_carte_wagon.piocher())
        self.plateau_de_jeu.cartes_wagon_visibles.append(\
            self.plateau_de_jeu.pioche_carte_wagon.piocher())

    def prendre_cartes_destinations(self):
        """ Methode abstraire permettant le choix d'une carte destination """
        pass

    def construire_route(self, depart, arrive):
        """
        Construit une route entre deux stations selon les regles du jeu CF: ManuelDuJoueur
        Retourne True si la route est construite, False si elle n'a pas pu etre construite
        """

        #On verifie que la route existe
        if not depart in self.plateau_de_jeu.graphe.adjacency_list or not\
            arrive in self.plateau_de_jeu.graphe.adjacency_list[depart]:

            return False

        #On verifie que l'on a bien toutes les cartes

