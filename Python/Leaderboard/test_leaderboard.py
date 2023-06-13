import unittest
from unittest import TestCase

from parameterized import parameterized

from leaderboard import *

# Test Data found via http://en.wikipedia.org/wiki/2015_Formula_One_season
driver1 = Driver(name="Nico Rosberg", country="DE")
driver2 = Driver(name="Lewis Hamilton", country="UK")
driver3 = Driver(name="Sebastian Vettel", country="DE")
driver4 = SelfDrivingCar(algorithm_version = "1.2", company="Acme")

race1 = Race("Australian Grand Prix", [driver1, driver2, driver3])
race2 = Race("Malaysian Grand Prix", [driver3, driver2, driver1])
race3 = Race("Chinese Grand Prix", [driver2, driver1, driver3])
race4 = Race("Fictional Grand Prix", [driver1, driver2, driver4])
race5 = Race("Fictional Grand Prix", [driver4, driver2, driver1])
driver4.algorithm_version = "1.3"
race6 = Race("Fictional Grand Prix", [driver2, driver1, driver4])


class TestLeaderboard(TestCase):

    def test_winner(self):
        leaderboard = Leaderboard(races=[race1, race2, race3])
        actual = leaderboard.driver_rankings()[0]
        self.assertEquals("Lewis Hamilton", actual)

    def test_driver_points(self):
        leaderboard = Leaderboard(races=[race4, race5, race6])
        actual = leaderboard.driver_points()["Lewis Hamilton"]
        self.assertEquals(18+18+25, actual)


class TestRace(TestCase):

    @parameterized.expand([
        (race1.points(driver1), 25),
        (race1.points(driver2), 18),
        (race1.points(driver3), 15)
    ])
    def test_driver_points(self, actual, expected):
        self.assertEquals(expected, actual)
