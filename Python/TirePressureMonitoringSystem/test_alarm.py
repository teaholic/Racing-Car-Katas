import unittest

from alarm import Alarm

class AlarmTest(unittest.TestCase):

    def test_alarm_is_off_by_default(self):
        alarm = Alarm()
        self.assertFalse(alarm.is_on)

    def test_set_alarm(self):
        alarm = Alarm()
        actual = alarm.set()

        self.assertTrue(actual.is_on)