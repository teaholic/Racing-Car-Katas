from unittest import TestCase

from parameterized import parameterized

from race import Race, Podium
from driver import Driver, SelfDrivingCar, DriverService
from leaderboard import Leaderboard, ScoringService

# Test Data found via http://en.wikipedia.org/wiki/2015_Formula_One_season
driver1 = Driver(id=1, name="Nico Rosberg", country="DE")
driver2 = Driver(id=2, name="Lewis Hamilton", country="UK")
driver3 = Driver(id=3, name="Sebastian Vettel", country="DE")
driver4 = DriverService().create(self_driving_car=SelfDrivingCar(id=4, algorithm_version = "1.2", company="Acme"))

driver_service = DriverService()
race1 = Race("Australian Grand Prix", Podium(first=driver1, second=driver2, third=driver3), driver_service)
race2 = Race("Malaysian Grand Prix", Podium(first=driver3, second=driver2, third=driver1), driver_service)
race3 = Race("Chinese Grand Prix", Podium(first=driver2, second=driver1, third=driver3), driver_service)
race4 = Race("Fictional Grand Prix", Podium(first=driver1, second=driver2, third=driver4), driver_service)
race5 = Race("Fictional Grand Prix", Podium(first=driver4, second=driver2, third=driver1), driver_service)
#driver4.algorithm_version = "1.3"
race6 = Race("Fictional Grand Prix", Podium(first=driver2, second=driver1, third=driver4), driver_service)


class TestLeaderboard(TestCase):

    def test_compute_rankings(self):
        scores = [
            Driver(id=1, name='Nico Rosberg', country='DE', points=58),
            Driver(id=2, name='Lewis Hamilton', country='UK', points=61),
            Driver(id=3, name='Sebastian Vettel', country='DE', points=0),
            Driver(id=4, name='Self Driving Car - Acme (1.2)', country='Acme', points=55)
        ]
        leaderboard = Leaderboard(scoring_service=ScoringService())
        actual = leaderboard.compute_rankings(scores)
        self.assertEquals("Lewis Hamilton", actual[0])

    def test_score_drivers(self):
        leaderboard = Leaderboard(scoring_service=ScoringService())
        updated_drivers = leaderboard.score_drivers(
            races=[race4, race5, race6],
            drivers=[driver1, driver2, driver3, driver4])
        hamilton = [driver for driver in updated_drivers if driver.name == "Lewis Hamilton"][0]
        self.assertEquals(18+18+25, hamilton.points)


class TestScoringService(TestCase):

    expected1 = [
        Driver(id=1, name='Nico Rosberg', country='DE', points=25),
        Driver(id=2, name='Lewis Hamilton', country='UK', points=18),
        Driver(id=3, name='Sebastian Vettel', country='DE', points=0),
        Driver(id=4, name='Self Driving Car - Acme (1.2)', country='Acme', points=15)
    ]
    expected2 = [
        Driver(id=1, name='Nico Rosberg', country='DE', points=15+25),
        Driver(id=2, name='Lewis Hamilton', country='UK', points=18+18),
        Driver(id=3, name='Sebastian Vettel', country='DE', points=0),
        Driver(id=4, name='Self Driving Car - Acme (1.2)', country='Acme', points=25+15)
    ]
    expected3 = [
        Driver(id=1, name='Nico Rosberg', country='DE', points=15+25+18),
        Driver(id=2, name='Lewis Hamilton', country='UK', points=18+18+25),
        Driver(id=3, name='Sebastian Vettel', country='DE', points=0),
        Driver(id=4, name='Self Driving Car - Acme (1.2)', country='Acme', points=25+15+15)
    ]

    @parameterized.expand([
        (race4, [driver1, driver2, driver3, driver4], expected1),
        (race5, expected1, expected2),
        (race6, expected2, expected3),
    ])
    def test_score_single_race(self, race, drivers, expected):
        actual = ScoringService()._score_single_race(race=race, drivers=drivers)
        self.assertEqual(actual[0], expected[0])
        self.assertEqual(actual[1], expected[1])
        self.assertEqual(actual[2], expected[2])
        self.assertEqual(actual[3], expected[3])

    def test_run(self):
        races = [race4, race5, race6]
        drivers = [driver1, driver2, driver3, driver4]
        expected = [
            Driver(id=1, name='Nico Rosberg', country='DE', points=15+25+18),
            Driver(id=2, name='Lewis Hamilton', country='UK', points=18+18+25),
            Driver(id=3, name='Sebastian Vettel', country='DE', points=0),
            Driver(id=4, name='Self Driving Car - Acme (1.2)', country='Acme', points=25+15+15)
        ]
        actual = ScoringService().run(races=races, drivers=drivers)
        self.assertEqual(actual[0], expected[0])
        self.assertEqual(actual[1], expected[1])
        self.assertEqual(actual[2], expected[2])
        self.assertEqual(actual[3], expected[3])
