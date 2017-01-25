#!/usr/bin/python3
from __future__ import print_function #retirer message d'avertissement pylint
from Joueur import Joueur
from Wagon import Wagon
class Humain(Joueur):
    """
    Classe representant un joueur controlle par un Humain
    """

    def prendre_cartes_destinations(self):
        """
        Pioche et demande au joueur quelles cartes destinations il souhaite
        Retourne True s'il a bien pioche et False si l'action ne s'est pas faite
        """
        # On pioche les cartes
        carte_destinations = []
        carte_destinations.append(self.plateau_de_jeu.pioche_carte_destination.piocher())
        carte_destinations.append(self.plateau_de_jeu.pioche_carte_destination.piocher())
        carte_destinations.append(self.plateau_de_jeu.pioche_carte_destination.piocher())

        print("Les cartes destinations sont:")
        for carte in carte_destinations:
            print(carte)

        # On fait choisir a l'utilisateur les cartes
        print("Quelles cartes choisissez vous ? (Minimum 1)")
        for carte in carte_destinations:
            choix_i = input("Voulez vous prendre la carte:", carte, "Oui(o)//Non(n)")

            if choix_i == 'o':
                self.cartes_destinations.append(carte)
            elif choix_i == 'n':
                pass
            else:
                print("Choix invalide, tanpis vous n'aurez pas la carte...")

        return True


    def jouer(self):
        super().jouer()
        action_fait = False

        while action_fait is False:
            choix = input("Que voulez-vous faire?\
            \n-Prendre des cartes Wagon (w)\
            \n-Prendre une carte locomotive (l)\
            \n-Prendre possession d'une route(r)\
            \n-Prendre des cartes destination supplementaires(d)\
            \n-Liste des routes possibles(rp)\
            \n-Affichage de la carte du jeu (c)")

            if choix == "w":  # Selection des deux cartes wagons
                choix_carte_1 = input("Quel est l'indice de la 1er carte selectionnee (0-4)?")
                choix_carte_2 = input("Quel est l'indice de la 2eme carte selectionnee(0-4)?")

                try:
                    choix_carte_1 = int(choix_carte_1)
                    choix_carte_2 = int(choix_carte_2)

                except:
                    continue

                if choix_carte_1 != choix_carte_2\
                    and choix_carte_1 >= 0\
                    and choix_carte_2 >= 0\
                    and choix_carte_1 <= 4\
                    and choix_carte_2 <= 4:

                    self.prendre_cartes_wagons(choix_carte_1, choix_carte_2)
                    print("Vous avez bien pioche deux cartes wagons")
                    action_fait = True
                else:
                    print("Les indices ne sont pas correctes")

            elif choix == "l":  # Pioche d'une locomotive
                self.cartes_wagons.append(Wagon("Multicolore"))
                print("Vous avez bien pioche une carte locomotive")
                action_fait = True

            elif choix == "r":  # Construction d'une nouvelle route
                print("Attention le chemin doit etre direct,\
                 de plus verifier bien que vous ayer les cartes necessaires")

                depart = input("Gare de depart?")
                arrive = input("Gare d'arrive?")
                couleur_choisie = input("Quelle couleur utilisee?")
                nombre_locomotive = input("Combien de locomotive?")

                try:
                    nombre_locomotive = int(nombre_locomotive)
                except:
                    continue

                if self.construire_route(depart, arrive, nombre_locomotive, couleur_choisie):
                    print("La route a bien ete construite")
                    action_fait = True
                else:
                    print("La route n'a pas ete construire")

            elif choix == "d":  # Choix de carte destination
                if self.prendre_cartes_destinations():
                    action_fait = True
                else:
                    print("Vous n'avez pas pus prendre de carte destinations")

            elif choix == "rp":  # On Affiche les routes encore constructibles
                print(self.plateau_de_jeu.construction_possible)

            elif choix == "c":  # On affiche la carte du jeu
                print(self.plateau_de_jeu.map)

            elif choix == "42":  # Commande cheat permettant d'avoir le plus court chemin entre deux gares
                depart = input("Gare de départ ?")
                arrive = input("Gare d'arrive ?")

                try:
                    dijsktra_resultat = self.plateau_de_jeu.map.dijkstra(depart)
                    print(dijsktra_resultat[arrive])
                except:
                    pass

            else:
                print("Le choix n'est pas valide")

            # On verifie que le joueur a plus de 2 wagons
        if self.dernier_tour:
            self.plateau_de_jeu.finir_partie()

        if self.reserve_wagon < 3:
            print("Plus qu'un seul tour!")
            self.dernier_tour = True

        input("Appuyer sur une touche pour faire jouer votre adversaire")
        self.adversaire.jouer()
