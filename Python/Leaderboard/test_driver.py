from unittest import TestCase

from driver import Driver, DriverFactory, SelfDrivingCar


class TestDriverFactory(TestCase):

    def test_create(self):
        expected = Driver(name="Self Driving Car - abc (1.0)", country="abc", points=0)
        actual = DriverFactory.create(SelfDrivingCar(algorithm_version="1.0", company="abc"))

        self.assertEqual(actual.name, expected.name)
        self.assertEqual(actual.country, expected.country)
        self.assertEqual(actual.points, expected.points)
