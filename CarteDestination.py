class CarteDestination(object):
    """ Class representant une carte destination du jeu """
    def __init__(self, depart, arrive, point):
        """
        :attribut self.depart: def self.depart to depart
        :attribut self.arrive: def self.depart to arrive
        """
        self.depart = depart
        self.arrive = arrive
        self.point = point

    def __repr__(self):

        return (self.depart + "--->" + self.arrive)
