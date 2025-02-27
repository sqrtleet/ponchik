import enum


@enum.unique
class ClientType(enum.Enum):
    regular = 1
    student = 2
    large_family = 3
    pensioner = 4
