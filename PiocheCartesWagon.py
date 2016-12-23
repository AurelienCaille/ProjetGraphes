import random
class PiocheCartesWagon:
    def __init__(self):

        self.pioche = []
        self.defausse = []


    def melangerPioche(self):

        self.pioche += self.defausse
        self.defausse = []
        
        random.shuffle(self.pioche)


    def piocher(self, nombreCarte = 1):

        if len(self.pioche == 0):
            self.melangerPioche()

        return self.pioche.pop()

    def __repr__(self):

        return "Pioche: " + str(self.pioche) + " Defausse: " + str(self.defausse)



if __name__ == "__main__":

    piocheCarte = PiocheCartesWagon()
    piocheCarte.pioche = [1,2,3]
    piocheCarte.defausse = [4,5]
    print (piocheCarte)
    piocheCarte.melangerPioche()
    print(piocheCarte)
