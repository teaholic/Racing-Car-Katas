from unittest import TestCase

from parameterized import parameterized

from driver import Driver, DriverService, SelfDrivingCar
from race import Race, Podium


class TestRace(TestCase):
    driver_service = DriverService()
    driver1 = Driver(id=1, name="Nico Rosberg", country="DE")
    driver2 = Driver(id=2, name="Lewis Hamilton", country="UK")
    driver3 = Driver(id=3, name="Sebastian Vettel", country="DE")
    driver4 = DriverService().create(self_driving_car=SelfDrivingCar(id=4, algorithm_version="1.2", company="Acme"))
    race1 = Race("Australian Grand Prix", Podium(first=driver1, second=driver2, third=driver3), driver_service)

    @parameterized.expand([
        (driver1, race1, 25),
        (driver2, race1, 18),
        (driver3, race1, 15),
        (driver4, race1, 0)
    ])
    def test_assign_point_to_first_driver(self, driver, race, expected):

        actual = race.assign_point(driver)
        self.assertEqual(actual.points, expected)