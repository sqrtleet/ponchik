import enum


@enum.unique
class ClientType(enum.Enum):
    REGULAR = "REGULAR"
    STUDENT = "STUDENT"
    LARGE_FAMILY = "LARGE_FAMILY"
    PENSIONER = "PENSIONER"
