from dataclasses import dataclass


@dataclass(frozen=True)
class Driver:
    name: str
    country: str
    points: int


@dataclass(frozen=True)
class SelfDrivingCar:
    algorithm_version: str
    company: str


class DriverFactory:

    def create(self_driving_car:SelfDrivingCar):
        return Driver(name = "Self Driving Car - {} ({})".format(self_driving_car.company, self_driving_car.algorithm_version), country=self_driving_car.company, points=0)
