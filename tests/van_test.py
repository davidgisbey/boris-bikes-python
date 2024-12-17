import pytest
from app.van import Van
from app.bike import Bike
from app.docking_station import DockingStation
from app.garage import Garage

def test_intialises_a_van_with_no_bikes():
  van = Van()
  assert van.bikes == []

def test_can_initialise_a_van_with_bikes():
  bike = Bike()
  van = Van(bikes=[bike])

  assert van.bikes == [bike]

def test_can_pickup_broken_bikes_from_docking_station():
  working_bike1 = Bike()
  working_bike2 = Bike()
  broken_bike1 = Bike(False)
  broken_bike2 = Bike(False)
  docking_station = DockingStation([working_bike1, working_bike2, broken_bike1, broken_bike2])
  van = Van()
  garage = Garage()

  van.retrieve_broken_bikes(docking_station, garage)

  assert docking_station.bikes == [working_bike1, working_bike2]
  assert van.bikes == []
  assert garage.bikes == [broken_bike1, broken_bike2]
