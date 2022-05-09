from enum import Enum


class DayOfWeek(Enum):
    MONDAY = MON = 'MON'
    TUESDAY = TUES = 'TUES'
    WEDNESDAY = WED = 'WED'
    THURSDAY = THUR = 'THUR'
    FRIDAY = FRI = 'FRI'
    SATURDAY = SAT = 'SAT'
    SUNDAY = SUN = 'SUN'

    def is_weekday(self) -> bool:
        """
        Return whether a given day is a weekday, i.e. it is neither
        saturday nor sunday.
        """
        return self in WEEKDAYS


WEEKDAYS = frozenset((
    DayOfWeek.MONDAY,
    DayOfWeek.TUESDAY,
    DayOfWeek.WEDNESDAY,
    DayOfWeek.THURSDAY,
    DayOfWeek.FRIDAY))

# WEEKDAYS = frozenset((
#     DayOfWeek.MONDAY, DayOfWeek.MON,
#     DayOfWeek.TUESDAY, DayOfWeek.TUES,
#     DayOfWeek.WEDNESDAY, DayOfWeek.WED,
#     DayOfWeek.THURSDAY, DayOfWeek.THUR,
#     DayOfWeek.FRIDAY, DayOfWeek.FRI))
