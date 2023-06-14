from unittest import TestCase

from parameterized import parameterized

from driver import Driver, DriverService, SelfDrivingCar


class TestDriverService(TestCase):

    def test_create(self):
        expected = Driver(id=1, name="Self Driving Car - abc (1.0)", country="abc", points=0)
        actual = DriverService().create(SelfDrivingCar(id=1, algorithm_version="1.0", company="abc"))

        self.assertEqual(actual.id, expected.id)
        self.assertEqual(actual.name, expected.name)
        self.assertEqual(actual.country, expected.country)
        self.assertEqual(actual.points, expected.points)

    @parameterized.expand([
        (Driver(id=1, name='n', country='IT', points=0), 1, 1),
        (Driver(id=1, name='n', country='IT', points=10), 5, 15)
    ])
    def test_score(self, driver, new_points, expected):
        actual = DriverService().score(driver=driver, new_points=new_points)
        self.assertEqual(actual.points, expected)
        self.assertEqual(actual.id, driver.id)