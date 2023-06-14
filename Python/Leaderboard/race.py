from dataclasses import dataclass
from enum import Enum

from driver import Driver, DriverService


class Points(Enum):
    First = 25
    Second = 18
    Third = 15


@dataclass(frozen=True)
class Podium:
    first: Driver
    second: Driver
    third: Driver


class Race:

    def __init__(self, name, results: Podium, driver_service: DriverService):
        self.name = name
        self.results = results
        self.driver_service = driver_service

    def assign_point(self, driver: Driver) -> Driver:
        if driver.id == self.results.first.id:
            return self.driver_service.score(driver=driver, new_points=Points.First.value)
        if driver.id == self.results.second.id:
            return self.driver_service.score(driver=driver, new_points=Points.Second.value)
        else:
            return self.driver_service.score(driver=driver, new_points=Points.Third.value)
