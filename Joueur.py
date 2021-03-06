
from __future__ import print_function #retirer message d'avertissement pylint
from Wagon import Wagon
class Joueur(object):
    """Classe abstraite representant un joueur"""
    def __init__(self, couleur):
        """
        :self.adversaire: init le joueur adverse de Joueur
        :self.score: represente le score du Joueur, commance a 1
        :self.cartes_wagons: init la liste vide de cartes wagon du joueur
        :self.cartes_destinations: init la lst vide de carte destination
        :self.reserve_wagon: init le stock de wagon de couleur du joueur
        :self.plateau_de_jeu: init a None le plateau de jeu associe au joueur
        self.plateau_de_jeu sera defini par l objet de classe plateau_de_jeu
        :self.couleur: represente la couleur du Joueur
        """

        self.adversaire = None
        self.score = 0
        self.cartes_wagons = []
        self.cartes_destinations = []
        self.reserve_wagon = 45
        self.plateau_de_jeu = None
        self.couleur = couleur
        self.dernier_tour = False
        self.point_possession_route = 0
        self.point_bonus_malus_destination = 0
        self.score_finale = 0

    def jouer(self):
        """ Methode abstraite lancant le tour du Joueur """
        print("-----------------------------------------------------------")
        print("Le joueur", self.couleur, "commence son tour")
        print("Le joueur a:")
        print("Cartes wagons:", self.cartes_wagons)
        print("Cartes destinations:", self.cartes_destinations)
    
    def calculer_score_finale(self):
        """ Calcule le score final du joueur selon les regles du jeu CF: ManuelDuJoueur"""
        # On somme les point des cartes objectif
        # Et des possessions de routes
        self.score_finale = self.point_bonus_malus_destination + self.point_possession_route
        return self.score_finale

    def prendre_cartes_wagons(self, indice_1, indice_2):
        """
        Selectionne 2 des cartes wagons visibles
        et complete les cartes manquantes sur le plateau de jeu
        """

        # On ajoute les cartes a la mains
        nouvelle_carte_1, nouvelle_carte_2 = self.plateau_de_jeu.piocher_cartes_wagon(indice_1, indice_2)

        print("Les cartes piochees sont:", nouvelle_carte_1, nouvelle_carte_2)

        self.cartes_wagons.append(nouvelle_carte_1)
        self.cartes_wagons.append(nouvelle_carte_2)

        # On revele deux nouvelles cartes
        self.plateau_de_jeu.cartes_wagon_visibles.append(\
            self.plateau_de_jeu.pioche_carte_wagon.piocher())
        self.plateau_de_jeu.cartes_wagon_visibles.append(\
            self.plateau_de_jeu.pioche_carte_wagon.piocher())

    def prendre_cartes_destinations(self):
        """ Methode abstraire permettant le choix d'une carte destination """
        pass

    def construire_route(self, depart, arrive, nombre_locomotive, couleur_desiree):

        """
        Construit une route entre deux stations selon les regles du jeu CF: ManuelDuJoueur
        Retourne True si la route est construite, False si elle n'a pas pu etre construite
        """

        longueur_route = None
        couleur_route = None

        # On verifie que la route existe
        if not depart in self.plateau_de_jeu.map.adjacency_list or not\
            arrive in self.plateau_de_jeu.map.adjacency_list[depart]:

            print("La route n'existe pas!!!")
            return False

        # On verifie que la route n'a pas ete deja construite
        if not (depart, arrive) in self.plateau_de_jeu.construction_possible\
        and not (arrive, depart) in self.plateau_de_jeu.construction_possible:

            print("La route a deja ete construite")
            return False

        # On recupere alors la longueur et couleur de la route
        for edge in self.plateau_de_jeu.map.edges:
            if edge[0] == depart and edge[1] == arrive:
                longueur_route = int(edge[2][0])
                couleur_route = edge[2][1]

        if couleur_route != "Gris" and couleur_route != couleur_desiree:
            print("La couleur de la route et la couleur desiree ne sont pas les memes !!!")
            return False

        # On verifie que l'on a assez de wagon
        if self.reserve_wagon < longueur_route:
            print("Le joueur n'a plus assez de wagon")
            return False

        # On verifie que l'on a bien toutes les cartes
        if not len([carte_wagon for carte_wagon in self.cartes_wagons if carte_wagon.couleur == "Multicolore"]) >= nombre_locomotive:

            print("Le joueur n'a pas le nombre de locomotive demandee!!!")
            return False

        if not len([carte_wagon for carte_wagon in self.cartes_wagons if carte_wagon.couleur == couleur_desiree]) >= longueur_route - nombre_locomotive:

            print("Le joueur n'a pas assez de carte wagon de la bonne couleur")
            return False

        # On construit la route et retire carte // wagon
        self.plateau_de_jeu.construction.add_an_edge(depart, arrive, self.couleur)

        self.reserve_wagon -= longueur_route

        for dummy_i in range(longueur_route - nombre_locomotive):
            self.cartes_wagons.remove(Wagon(couleur_desiree))
        for dummy_i in range(nombre_locomotive):
            self.cartes_wagons.remove(Wagon("Multicolore"))

        self.plateau_de_jeu.construction_possible.remove((depart, arrive))
        self.plateau_de_jeu.construction_possible.remove((arrive, depart))

        # On compte les points de possesion de route
        if longueur_route == 1:
            self.point_possession_route += 1
        elif longueur_route == 2:
            self.point_possession_route += 2
        elif longueur_route == 3:
            self.point_possession_route += 4
        elif longueur_route == 4:
            self.point_possession_route += 7
        elif longueur_route == 5:
            self.point_possession_route += 11
        elif longueur_route == 6:
            self.point_possession_route += 15
        elif longueur_route == 7:
            self.point_possession_route += 19
        elif longueur_route == 8:
            self.point_possession_route += 21
        print("vous avez ", self.point_possession_route, " points de routes")

        # On comptabilise les points de bonus d objectif
        for carte in self.cartes_destinations:
            if depart == carte.depart and arrive == carte.arrive:
                self.point_bonus_malus_destination += 2*(carte.point)
                print("bonus ou malus de point objectif: ", self.point_bonus_malus_destination)
        return True
