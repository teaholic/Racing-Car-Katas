import unittest

from alarm import Alarm

class AlarmTest(unittest.TestCase):

    def test_alarm_is_off_by_default(self):
        alarm = Alarm()
        self.assertFalse(alarm.is_on)

    def test_set_alarm(self):
        actual = Alarm(is_on=True)

        self.assertTrue(actual.is_on)