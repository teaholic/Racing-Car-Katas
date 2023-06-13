from sensor import Sensor
from alarm import Alarm


class TirePressureMonitoringService():

    def __init__(self, low_pressure_threshold, high_pressure_threshold):
        self._low_pressure_threshold = low_pressure_threshold
        self._high_pressure_threshold = high_pressure_threshold

    def check(self, psi_pressure_value) -> bool:
        if psi_pressure_value < self._low_pressure_threshold \
                or self._high_pressure_threshold < psi_pressure_value:
            return True


class TirePressureMonitoringSystem(object):

    def __init__(self):
        self._sensor = Sensor()
        self._alarm = Alarm()
        self._low_pressure_threshold = 17
        self._high_pressure_threshold = 21
        self._service = TirePressureMonitoringService(low_pressure_threshold=self._low_pressure_threshold, high_pressure_threshold=self._high_pressure_threshold)
        
    def run(self) -> Alarm:
        psi_pressure_value = self._sensor.pop_next_pressure_psi_value()
        is_alarm = self._service.check(psi_pressure_value)
        return Alarm(is_on=is_alarm)
