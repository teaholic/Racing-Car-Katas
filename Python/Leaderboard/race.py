from dataclasses import dataclass
from enum import Enum

from driver import Driver


class Points(Enum):
    First = 25
    Second = 18
    Third = 15


@dataclass(frozen=True)
class Results:
    first: Driver
    second: Driver
    third: Driver

class Race:

    def __init__(self, name, results: Results):
        self.name = name
        self.results = results