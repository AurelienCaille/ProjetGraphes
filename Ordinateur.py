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
        resultat = (float('inf'), (None, None))  # resultat = (longueur, chemin)
        couleur = None
        if len(self.cartes_destinations) > 0:
            route_a_construire = []
            for carte_destination in self.cartes_destinations:
                depart = carte_destination.depart
                arrive = carte_destination.arrive

                # On prend le chemin le plus court, on le decompose
                # et on regarde si la route est constructible
                chemin = self.plateau_de_jeu.map.dijkstra(depart)[arrive]
                for i in range(len(chemin[0]) - 1):
                    if chemin[0][i] < resultat[0] and (chemin[1][i], chemin[1][i+1]) in self.plateau_de_jeu.construction_possible:  # Ne fonctionne pas lors de route double
                        resultat = (chemin[0][i], (chemin[1][i], chemin[1][i+1]))
                        for child in self.plateau_de_jeu.map.adjacency_list_valued[chemin[1][i]]:  # On recupere la couleur associee
                            if child[0] == chemin[1][i+1]:
                                couleur = child[1][1]



        else:
            # On pioche 1 seule carte_destination  # Strategie A DEFINIR
            print("L'Ordinateur pioche une carte_destination")
            if len(self.plateau_de_jeu.pioche_carte_destination.pioche) is not None:
                self.cartes_destinations.append(self.plateau_de_jeu.pioche_carte_destination.piocher())
            print("_____________________________")
            self.adversaire.jouer()

        depart = resultat[1][0]
        arrive = resultat[1][1]
        print("Je veux construire", resultat, couleur)
        print("J'ai les cartes wagons", self.cartes_wagons)

        # On verifie si on peut construire le chemin le plus court
        # On verifie que l'on a bien toutes les cartes et on construit alors la route
        if len([carte_wagon for carte_wagon in self.cartes_wagons if carte_wagon.couleur == couleur]) > resultat[0]:
            print("L'Ordinateur tente de construire la route", resultat)
            if self.construire_route(depart, arrive, 0, couleur):  # !!!! NE PREND PAS EN COMPTE LES ROUTES GRISES
                print("L'Ordinateur a bien construit la route")
            else:
                print("L'or n'a pas reussi a construire la route")
            print("_____________________________")
            self.adversaire.jouer()
        else:
            print("L'ordinateur prend deux cartes wagons")
            if len(self.plateau_de_jeu.pioche_carte_wagon.pioche) is not None:
                self.prendre_cartes_wagons(0, 1) # !!!!!! NE CHOISIS PAS LES WAGONS CORRECTEMENTS
            else:
                print("Oups ma super strategie n'est pas possible.. il n'y a plus de carte wagon disponible")
            print("_____________________________")
            self.adversaire.jouer()
