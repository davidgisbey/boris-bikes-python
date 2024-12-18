class Garage:
    def __init__(self, bikes=[]):
        self.bikes = bikes

    def repair_bikes(self):
        for bike in self.bikes:
            if bike.working == False:
              bike.working = True
