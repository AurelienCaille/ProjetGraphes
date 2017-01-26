import random
from CarteDestination import CarteDestination
class PiocheCarteDestination(object):
    """ Classe representant une piochde de carte destination"""
    def __init__(self):
        """
        :attribut self.pioche: init la pile de carte destination vide
        """

        self.pioche = []
        self.open_file()
        self.melanger()

    def melanger(self):
        """
        randomise l ordre des carte dans la liste
        """
        random.shuffle(self.pioche)

    def piocher(self):
        """
        supprime une carte de la pile de carte, et le renvoie
        """
        return self.pioche.pop()

    def __repr__(self):
        """
        return la lst de la pile
        """
        return str(self.pioche)

    def open_file(self):
        """ Ouvre le fichier contenant la liste des cartes destinations """

        file_destination = open("cartes_objectifs_-_version_epuree.csv", "r", encoding='utf8')
        file_destination = file_destination.read()
        file_destination = file_destination.split("\n")[1:]

        for lign in file_destination:
            lign_split = lign.split(":")

            if len(lign_split) == 3:
                depart = lign_split[0]
                arrive = lign_split[1]
                point = lign_split[2]
                self.pioche.append(CarteDestination(depart, arrive, point))

if __name__ == '__main__':

    pioche_carte = PiocheCarteDestination()
    pioche_carte.pioche = [1, 2, 3]
    pioche_carte.melanger()
    print(pioche_carte)
    print(pioche_carte.piocher())
    print(pioche_carte)
