from sensor import Sensor
from alarm import Alarm, AlarmService


class TirePressureMonitoringSystem(object):

    def __init__(self):
        self._sensor = Sensor()
        self.alarm = Alarm()
        self._low_pressure_threshold = 17
        self._high_pressure_threshold = 21
        self._service = AlarmService(low_pressure_threshold=self._low_pressure_threshold, high_pressure_threshold=self._high_pressure_threshold)
        
    def run(self) -> Alarm:
        psi_pressure_value = self._sensor.pop_next_pressure_psi_value()
        self.alarm = self._service.check(psi_pressure_value)
