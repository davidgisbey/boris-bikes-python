class DockingStation:
    def __init__(self, bikes=[], capacity=20):
        self.bikes = bikes
        self.capacity = capacity

    def release_bike(self, bike):
        if bike not in self.bikes:
            return "Bike not in docking station"

        if bike.working == False:
            return "Bike is not working"

        self.bikes.remove(bike)
        return bike

    def receive_bike(self, bike, working=True):
        if len(self.bikes) >= self.capacity:
            return "Docking station is full"

        bike.working = working
        self.bikes.append(bike)
        return True
