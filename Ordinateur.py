from Joueur import Joueur
from CarteDestination import CarteDestination
class Ordinateur(Joueur):
    """
    Classe representant un joueur controlle par un Ordinateur
    """
    def jouer(self):
        """
        L'ordinateur va jouer selon un comportement predefini route>carte_wagon // carte_destination
        """
        # L'ordinateur cherche le chemin le plus court a construire selon ses cartes destinations
        # s'il lui en reste sinon il en pioche
        # S'il a les cartes il construit la route sinon il pioche des wagons//locomotive

        # Recherche du chemin le plus court parmis les cartes destinations
        resultat = (float('inf'), None)  # resultat = (longueur, chemin)
        if len(self.cartes_destinations) > 0:
            for carte_destination in self.cartes_destinations:
                depart = carte_destination.depart
                arrive = carte_destination.arrive

                dijkstra_resultat = self.plateau_de_jeu.map.dijkstra(depart)

                if dijkstra_resultat[arrive][0] < resultat[0]:
                    resultat = dijkstra_resultat[arrive]
        else:
            # On pioche 1 seule carte_destination  # Strategie A DEFINIR
            pass
            self.adversaire.jouer()

        # On verifie si on peut construire le chemin le plus court
        couleur_route = self.plateau_de_jeu.map.adjacency_list_valued[depart][1]

        # On verifie que l'on a bien toutes les cartes et on construit alors la route
        if len([carte_wagon for carte_wagon in self.cartes_wagons if carte_wagon.couleur == couleur_route]):
            self.construire_route(depart, arrive, 0, couleur_route)  # !!!! NE PREND PAS EN COMPTE LES ROUTES GRISES
            self.adversaire.jouer()
        else:
            self.prendre_cartes_wagons(0, 1) # !!!!!! NE CHOISIS PAS LES WAGONS CORRECTEMENTS
            self.adversaire.jouer()







        self.adversaire.jouer()
