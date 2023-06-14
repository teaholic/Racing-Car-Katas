from collections import defaultdict
from dataclasses import dataclass
from typing import List

from Python.Leaderboard.driver import DriverService
from race import Race


class Leaderboard(object):
    
    def __init__(self, races: List[Race], drivers: dict, driver_service: DriverService):
        self.races = races
        self.drivers = drivers
        self.driver_service = driver_service

    def score_driver_points(self):
        for race in self.races:
            driver = race.results.first



    def driver_rankings(self):
        rankings = sorted(self.driver_points().items(), key=lambda x: x[1], reverse=True)
        return [name for (name, points) in rankings]

