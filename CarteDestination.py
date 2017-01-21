class CarteDestination:
    def __init__(self, depart, arrive):
        """
        :attribut self.depart: def self.depart to depart 
        :attribut self.arrive: def self.depart to arrive
        """
        self.depart = depart
        self.arrive = arrive
        
    def __repr__(self):
        
        return (self.depart + "--->" + self.arrive)
