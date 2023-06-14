from dataclasses import dataclass


@dataclass(frozen=True)
class Driver:
    id: int
    name: str
    country: str
    points: int = 0


@dataclass(frozen=True)
class SelfDrivingCar:
    id: int
    algorithm_version: str
    company: str


class DriverService:

    def create(self, self_driving_car:SelfDrivingCar) -> Driver:
        return Driver(id=self_driving_car.id, name="Self Driving Car - {} ({})".format(self_driving_car.company, self_driving_car.algorithm_version), country=self_driving_car.company, points=0)

    def score(self, driver: Driver, new_points: int) -> Driver:
        return Driver(id=driver.id, name=driver.name, country=driver.country, points=driver.points+new_points)
