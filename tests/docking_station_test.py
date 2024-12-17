import pytest
from app.docking_station import DockingStation

def test_docking_station_initialises_with_empty_array_for_bikes():
  docking_station = DockingStation()
  assert docking_station.bikes == []

def test_pass_bikes_in_on_initialisation():
  docking_station = DockingStation(['bike1', 'bike2'])
  assert docking_station.bikes == ['bike1', 'bike2']

