from collections import defaultdict
from dataclasses import dataclass


class Leaderboard(object):
    
    def __init__(self, races):
        self.races = races

    def driver_points(self):
        driver_points = defaultdict(int)
        for race in self.races:
            for driver in race.results:
                name = race.driver_name(driver)
                driver_points[name] += race.points(driver)
        return driver_points

    def driver_rankings(self):
        rankings = sorted(self.driver_points().items(), key=lambda x: x[1], reverse=True)
        return [name for (name, points) in rankings]

