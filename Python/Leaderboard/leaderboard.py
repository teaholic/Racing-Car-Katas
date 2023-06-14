import operator
from typing import List

from driver import Driver
from race import Race


class ScoringService:

    def run(self, races: List[Race], drivers: List[Driver]) -> List[Driver]:
        updated_drivers = drivers
        for race in races:
            results = self._score_single_race(race, updated_drivers)
            updated_drivers = results
        return updated_drivers

    def _score_single_race(self, race: Race, drivers: List[Driver]) -> List[Driver]:
        updated_drivers = []
        for driver in drivers:
            result = race.assign_point(driver=driver)
            updated_drivers.append(result)
        return updated_drivers


class Leaderboard(object):
    
    def __init__(self, scoring_service: ScoringService):
        self.scoring_service = scoring_service

    def score_drivers(self, races: List[Race], drivers: List[Driver]):
        return self.scoring_service.run(races=races, drivers=drivers)

    def compute_rankings(self, scores: List[Driver]):
        rankings = sorted(scores, key=operator.attrgetter('points'), reverse=True)
        return [driver.name for driver in rankings]
