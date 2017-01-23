#!/usr/bin/python3
from __future__ import print_function #retirer message d'avertissement pylint
from Joueur import Joueur
from Wagon import Wagon
class Humain(Joueur):
    """
    Classe representant un joueur controlle par un Humain
    """

    def jouer(self):
        super().jouer()
        action_fait = False

        while action_fait is False:
            choix = input("Que voulez-vous faire?\
            \n-Prendre des cartes Wagon (w)\
            \n-Prendre une carte locomotive (l)\
            \n-Prendre possession d'une route(r)\
            \n-Prendre des cartes destination supplementaires(d)")

            if choix == "w":  # Selection des deux cartes wagons
                choix_carte_1 = input("Quel est l'indice de la 1er carte selectionnee?")
                choix_carte_2 = input("Quel est l'indice de la 2eme carte selectionnee?")

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

            elif choix == "d":
                pass
            else:
                print("Le choix n'est pas valide")

