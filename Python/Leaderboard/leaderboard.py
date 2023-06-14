import operator
from dataclasses import dataclass
from typing import List

from driver import DriverService, Driver
from race import Race


class ParticipantsService:

    def after(self, race: Race, drivers: List[Driver]):
        updated_drivers = []
        for driver in drivers:
            result = race.assign_point(driver=driver)
            updated_drivers.append(result)
        return updated_drivers


class Leaderboard(object):
    
    def __init__(self, races: List[Race], drivers: List[Driver], driver_service: DriverService, participants_service: ParticipantsService):
        self.races = races
        self.drivers = drivers
        self.driver_service = driver_service
        self.participants_service = participants_service

    def score_drivers(self):
        updated_drivers = []
        for race in self.races:
            results = self.participants_service.after(race, self.drivers)
            for result in results:
                updated_drivers.append(result)
        self.drivers = updated_drivers

    def driver_rankings(self):
        rankings = sorted(self.drivers, key=operator.attrgetter('points'), reverse=True)
        return [name for (name, points) in rankings]

