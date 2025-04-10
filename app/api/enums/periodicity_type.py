import enum


@enum.unique
class PeriodicityType(enum.Enum):
    OneTimeVisit = 1
    TwoTimesAWeek = 2
    ThreeTimesAWeek = 3
