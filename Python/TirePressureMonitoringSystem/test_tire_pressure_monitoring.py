from unittest import TestCase
from unittest.mock import patch

from sensor import Sensor
from tire_pressure_monitoring import TirePressureMonitoringService, TirePressureMonitoringSystem


class TestTirePressureMonitoringService(TestCase):

    def test_check_low_pressure(self):
        service = TirePressureMonitoringService(low_pressure_threshold=5, high_pressure_threshold=7)
        actual = service.check(3)
        self.assertTrue(actual)

    def test_check_high_pressure(self):
        service = TirePressureMonitoringService(low_pressure_threshold=5, high_pressure_threshold=7)
        actual = service.check(8)
        self.assertTrue(actual)

    def test_check_regular_pressure(self):
        service = TirePressureMonitoringService(low_pressure_threshold=5, high_pressure_threshold=7)
        actual = service.check(6)
        self.assertFalse(actual)

class TestTirePressureMonitoringSystem(TestCase):

    @patch.object(Sensor, "pop_next_pressure_psi_value")
    def test_check_low_pressure_and_raise_alarm(self, sensor):
        sensor.return_value = 10
        actual = TirePressureMonitoringSystem().run()

        self.assertTrue(actual.is_on)

    @patch.object(Sensor, "pop_next_pressure_psi_value")
    def test_check_high_pressure_and_raise_alarm(self, sensor):
        sensor.return_value = 22
        actual = TirePressureMonitoringSystem().run()

        self.assertTrue(actual.is_on)

    @patch.object(Sensor, "pop_next_pressure_psi_value")
    def test_check_regular_pressure_and_do_nothing(self, sensor):
        sensor.return_value = 19
        actual = TirePressureMonitoringSystem().run()

        self.assertFalse(actual.is_on)