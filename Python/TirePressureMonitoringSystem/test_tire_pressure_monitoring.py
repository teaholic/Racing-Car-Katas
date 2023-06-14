from unittest import TestCase
from unittest.mock import patch

from sensor import Sensor
from tire_pressure_monitoring import TirePressureMonitoringSystem


class TestTirePressureMonitoringSystem(TestCase):

    @patch.object(Sensor, "pop_next_pressure_psi_value")
    def test_check_low_pressure_and_raise_alarm(self, sensor):
        sensor.return_value = 10
        system = TirePressureMonitoringSystem()
        system.run()

        self.assertTrue(system.alarm.is_on)

    @patch.object(Sensor, "pop_next_pressure_psi_value")
    def test_check_high_pressure_and_raise_alarm(self, sensor):
        sensor.return_value = 22
        system = TirePressureMonitoringSystem()
        system.run()

        self.assertTrue(system.alarm.is_on)

    @patch.object(Sensor, "pop_next_pressure_psi_value")
    def test_check_regular_pressure_and_do_nothing(self, sensor):
        sensor.return_value = 19
        system = TirePressureMonitoringSystem()
        system.run()

        self.assertFalse(system.alarm.is_on)
