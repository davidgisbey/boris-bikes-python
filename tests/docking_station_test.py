import pytest
from app.docking_station import DockingStation
from app.bike import Bike

def test_docking_station_initialises_with_empty_array_for_bikes():
  docking_station = DockingStation()
  assert docking_station.bikes == []

def test_pass_bikes_in_on_initialisation():
  docking_station = DockingStation(['bike1', 'bike2'])
  assert docking_station.bikes == ['bike1', 'bike2']

def test_can_release_bike():
  bike1 = Bike()
  bike2 = Bike()
  bike3 = Bike()
  docking_station = DockingStation([bike1, bike2, bike3])

  released_bike1 = docking_station.release_bike(bike1)
  released_bike2 = docking_station.release_bike(bike3)

  assert released_bike1 == bike1
  assert released_bike2 == bike3
  assert docking_station.bikes == [bike2]

def test_bike_not_in_docking_station():
  bike1 = Bike()
  docking_station = DockingStation()

  assert docking_station.release_bike(bike1) == "Bike not in docking station"

def test_cannot_release_broken_bike():
  bike = Bike(False)
  docking_station = DockingStation(bikes=[bike])

  assert(docking_station.release_bike(bike)) == "Bike is not working"

def test_can_receive_bike():
  bike = Bike()
  docking_station = DockingStation()

  assert docking_station.receive_bike(bike) == True
  assert docking_station.bikes == [bike]

def test_cannot_receive_bike_if_full():
  bike = Bike()
  docking_station = DockingStation(bikes=[], capacity=0)

  assert docking_station.receive_bike(bike) == "Docking station is full"
  assert docking_station.bikes == []

def test_can_report_bike_broken():
  bike = Bike(working=True)
  docking_station = DockingStation(bikes=[])

  docking_station.receive_bike(bike, False)

  assert docking_station.bikes == [bike]
  assert docking_station.bikes[0].working == False
