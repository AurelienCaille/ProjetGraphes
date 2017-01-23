import random
class PiocheCarteDestination(object):
    """ Classe representant une piochde de carte destination"""
    def __init__(self):
        """
        :attribut self.pioche: init la pile de carte destination vide
        """

        self.pioche = []

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

if __name__ == '__main__':

    pioche_carte = PiocheCarteDestination()
    pioche_carte.pioche = [1, 2, 3]
    pioche_carte.melanger()
    print(pioche_carte)
    print(pioche_carte.piocher())
    print(pioche_carte)
