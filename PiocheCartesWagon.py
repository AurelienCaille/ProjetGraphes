import random
from Wagon import Wagon
COULEURS = ["Bleu", "Rose", "Orange", "Blanc", "Vert", "Jaune", "Noir", "Rouge"]
class PiocheCartesWagon:
    def __init__(self):
        """
        :self.pioche: init la liste vide d element dans la pile de carte
        :self.defausse: init la liste vide de carte dans la defausse
        """

        self.pioche = []
        self.defausse = []

        # On ajoute les cartes wagons

        for couleur in COULEURS:
            for dummy_i in range(12):
                self.pioche.append(Wagon(couleur))

        self.melangerPioche()


    def melangerPioche(self):
        """
        reintegre la defausse dans la pile de carte wagon, puis randomise
        l ordre des carte
        """
        self.pioche += self.defausse
        self.defausse = []

        random.shuffle(self.pioche)


    def piocher(self):
        """
        supprime et retourne un element de la pile de cartes wagons
        """

        if len(self.pioche) == 0:
            self.melangerPioche()

        return self.pioche.pop()

    def __repr__(self):
        """
        renvoie l etat de la pioche et de la defusse de cartes wagons
        """
        return "Pioche: " + str(self.pioche) + " Defausse: " + str(self.defausse)



if __name__ == "__main__":

    piocheCarte = PiocheCartesWagon()
    piocheCarte.pioche = [1,2,3]
    piocheCarte.defausse = [4,5]
    print (piocheCarte)
    piocheCarte.melangerPioche()
    print(piocheCarte)
