class Van:
  def __init__(self, bikes = []):
    self.bikes = bikes

  def retrieve_broken_bikes(self, docking_station, garage):
    self.__retrieve_bikes_from_docking_station(docking_station)
    self.__drop_bikes_off_at_garage(garage)

  def __retrieve_bikes_from_docking_station(self, docking_station):
    broken_bikes = [bike for bike in docking_station.bikes if not bike.working]
    self.bikes.extend(broken_bikes)
    for bike in broken_bikes:
      docking_station.bikes.remove(bike)

  def __drop_bikes_off_at_garage(self, garage):
    garage.bikes.extend(self.bikes)
    self.bikes = []
