import enum


@enum.unique
class SubscriptionStatusType(enum.Enum):
    active = 1
    closed = 2
    paused = 3
