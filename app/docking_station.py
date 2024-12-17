class DockingStation:
  def __init__(self, bikes = []):
    self.bikes = bikes

  def release_bike(self, bike):
    if bike not in self.bikes:
      return "Bike not in docking station"

    self.bikes.remove(bike)
    return bike
