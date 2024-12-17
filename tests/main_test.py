import pytest
from app.main import DockingStation

def test_docking_station_initialises_with_empty_array_for_bikes():
  docking_station = DockingStation()
  assert docking_station.bikes == []

