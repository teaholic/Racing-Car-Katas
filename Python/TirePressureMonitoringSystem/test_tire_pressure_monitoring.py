import unittest

from tire_pressure_monitoring import Alarm

class AlarmTest(unittest.TestCase):

    def test_alarm_is_off_by_default(self):
        alarm = Alarm()
        assert not alarm.is_alarm_on

    def test_set_alarm(self):
        alarm = Alarm()
        actual = alarm.set()

        self.assertTrue(actual.is_alarm_on)