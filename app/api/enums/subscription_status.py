import enum


@enum.unique
class SubscriptionStatusType(enum.Enum):
    active = 1
    cloased = 2
    paused = 3
