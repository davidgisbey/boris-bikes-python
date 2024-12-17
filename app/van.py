class Van:
  def __init__(self, bikes = []):
    self.bikes = bikes

  def retrieve_broken_bikes(self, docking_station):
    broken_bikes = [bike for bike in docking_station.bikes if not bike.working]
    self.bikes.extend(broken_bikes)
    for bike in broken_bikes:
      docking_station.bikes.remove(bike)

