from enum import Enum


class Status(Enum):
    ROOT = 0
    ADMIN = 1
    STORAGE = 2
    VOLUNTEER = 3
    PRESS_SERVICE = 4


def check_status(requester_status: int, asking_status: int) -> bool:
    if requester_status > asking_status:
        return False
    else:
        return True
