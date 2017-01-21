class CarteDestination:
    def __init__(self, depart, arrive):
        self.depart = depart
        self.arrive = arrive
        
    def __repr__(self):
        
        return (self.depart + "--->" + self.arrive)
