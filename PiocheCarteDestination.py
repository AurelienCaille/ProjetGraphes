import random
class PiocheCarteDestination:
    """ Classe representant une piochde de carte destination"""
    def __init__(self):

        self.pioche = []

    def melanger(self):

        random.shuffle(self.pioche)

    def piocher(self):

        return self.pioche.pop()

    def __repr__(self):

        return str(self.pioche)

if __name__ == '__main__':

    piocheCarte = PiocheCarteDestination()
    piocheCarte.pioche = [1,2,3]
    piocheCarte.melanger()
    print(piocheCarte)
    print(piocheCarte.piocher())
    print(piocheCarte)
