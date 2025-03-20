import enum


@enum.unique
class ClientType(enum.Enum):
    REGULAR = 1
    STUDENT = 2
    LARGE_FAMILY = 3
    PENSIONER = 4
