from dataclasses import dataclass


@dataclass(frozen=True)
class Alarm:
    is_on: bool = False


class AlarmService:

    def __init__(self, low_pressure_threshold, high_pressure_threshold):
        self._low_pressure_threshold = low_pressure_threshold
        self._high_pressure_threshold = high_pressure_threshold

    def check(self, psi_pressure_value) -> Alarm:
        if psi_pressure_value < self._low_pressure_threshold \
                or self._high_pressure_threshold < psi_pressure_value:
            return Alarm(is_on=True)
        else:
            return Alarm(is_on=False)
