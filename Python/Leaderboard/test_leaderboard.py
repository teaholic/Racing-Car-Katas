import unittest
from unittest import TestCase

from parameterized import parameterized

from race import Race, Podium
from driver import Driver, SelfDrivingCar, DriverService
from leaderboard import Leaderboard

# Test Data found via http://en.wikipedia.org/wiki/2015_Formula_One_season
driver1 = Driver(id=1, name="Nico Rosberg", country="DE")
driver2 = Driver(id=2, name="Lewis Hamilton", country="UK")
driver3 = Driver(id=3, name="Sebastian Vettel", country="DE")
driver4 = DriverService.create(SelfDrivingCar(id=4, algorithm_version = "1.2", company="Acme"))

driver_service = DriverService()
race1 = Race("Australian Grand Prix", Podium(first=driver1, second=driver2, third=driver3), driver_service)
race2 = Race("Malaysian Grand Prix", Podium(first=driver3, second=driver2, third=driver1), driver_service)
race3 = Race("Chinese Grand Prix", Podium(first=driver2, second=driver1, third=driver3), driver_service)
race4 = Race("Fictional Grand Prix", Podium(first=driver1, second=driver2, third=driver4), driver_service)
race5 = Race("Fictional Grand Prix", Podium(first=driver4, second=driver2, third=driver1), driver_service)
#driver4.algorithm_version = "1.3"
race6 = Race("Fictional Grand Prix", Podium(first=driver2, second=driver1, third=driver4), driver_service)


class TestLeaderboard(TestCase):

    def test_winner(self):
        leaderboard = Leaderboard(races=[race1, race2, race3], drivers=[driver1, driver2, driver3, driver4])
        actual = leaderboard.driver_rankings(0)
        self.assertEquals("Lewis Hamilton", actual)

    def test_driver_points(self):
        leaderboard = Leaderboard(races=[race4, race5, race6], drivers=[driver1, driver2, driver3, driver4])
        actual = leaderboard.score_driver_points("Lewis Hamilton")
        self.assertEquals(18+18+25, actual)


class TestRace(TestCase):

    @parameterized.expand([
        (race1.points(driver1), 25),
        (race1.points(driver2), 18),
        (race1.points(driver3), 15)
    ])
    def test_driver_points(self, actual, expected):
        self.assertEquals(expected, actual)
