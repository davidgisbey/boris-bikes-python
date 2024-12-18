import pytest
from app.garage import Garage
from app.bike import Bike

def test_intialises_with_an_empty_bikes_array():
    garage = Garage()
    assert garage.bikes == []

def test_can_initialise_with_bikes():
    bike = Bike()
    garage = Garage([bike])
    assert garage.bikes == [bike]

def test_can_repair_bikes():
    bike = Bike(working=False)
    garage = Garage([bike])

    garage.repair_bikes()
    assert garage.bikes[0].working == True
