import pytest
from app.bike import Bike

def test_intialises_an_instance_of_bike():
  bike = Bike()
  assert type(bike) is Bike

