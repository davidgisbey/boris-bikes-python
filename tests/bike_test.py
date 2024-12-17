import pytest
from app.bike import Bike


def test_intialises_a_working_bike_by_default():
    bike = Bike()
    assert bike.working == True


def test_can_initialise_a_broken_bike():
    bike = Bike(working=False)
    assert bike.working == False
