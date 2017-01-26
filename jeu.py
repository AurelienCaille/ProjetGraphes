from PlateauDeJeu import PlateauDeJeu
from Humain import Humain
from Ordinateur import Ordinateur


if __name__ == "__main__":

    # On cree les deux joueurs
    joueur_1 = Humain("Bleu")
    joueur_2 = None

    print("Les aventuriers du rail: initialisation de la partie")

    choix_ordinateur = False

    while choix_ordinateur is False:
        input_ordinateur = input("Voulez vous inclure un Ordinateur: Oui(o) Non(n) ? ")

        if input_ordinateur == "o":
            choix_ordinateur = True
            joueur_2 = Ordinateur("Vert")
        elif input_ordinateur == "n":
            choix_ordinateur = True
            joueur_2 = Humain("Rouge")
        else:
            print("Choix impossible!")

    # On cree le plateau du jeu
    plateau = PlateauDeJeu(joueur_1, joueur_2)
    joueur_1.plateau_de_jeu = plateau
    joueur_2.plateau_de_jeu = plateau

    # On lance la partie
    plateau.jouer()
