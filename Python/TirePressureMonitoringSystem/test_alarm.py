from unittest import TestCase

from alarm import Alarm, AlarmService


class TestAlarm(TestCase):

    def test_alarm_is_off_by_default(self):
        alarm = Alarm()
        self.assertFalse(alarm.is_on)

    def test_set_alarm(self):
        actual = Alarm(is_on=True)

        self.assertTrue(actual.is_on)

class TestAlarmService(TestCase):

    def test_check_low_pressure(self):
        service = AlarmService(low_pressure_threshold=5, high_pressure_threshold=7)
        actual = service.check(3)
        self.assertTrue(actual.is_on)

    def test_check_high_pressure(self):
        service = AlarmService(low_pressure_threshold=5, high_pressure_threshold=7)
        actual = service.check(8)
        self.assertTrue(actual.is_on)

    def test_check_regular_pressure(self):
        service = AlarmService(low_pressure_threshold=5, high_pressure_threshold=7)
        actual = service.check(6)
        self.assertFalse(actual.is_on)