from collections import namedtuple
from typing import List


# TODO: write TimeSlot usin attrs:
# https://www.attrs.org/en/stable/index.html
class TimeSlot(namedtuple("TimeSlot", "code weekday timespan kind")):  # noqa
    def __eq__(self, other):
        return all([getattr(self, f) == getattr(other, f) for f in self._fields])


class TimetableInterface:
    """ Interface of a timetable
    """

    # -- Abstract Methods
    def gen_timeslot(self, code: str, weekday_int: int) -> TimeSlot:
        """ Generate a timeslot object based on the given information
            code: code name of this timeslot
            weekday_int: 1-7 (Mon-Sun)

            kind: which kind of system it use
        """
        # Some things that a child class might need to take care:
        #   + populate the `kind` field of the TimeSlot
        #   + translate the weekday_int into the actual weekday by self._to_weekday
        raise NotImplementedError()

    def get_kind(self) -> str:
        """ Which type of TimeTable it is describing.
        """
        raise NotImplementedError()

    def is_valid_code(self, code) -> bool:
        """ check if this code is valid inside this table
        """
        raise NotImplementedError()

    def get_valid_codes(self) -> List[str]:
        """ return the code that this table is able to translate its timespan
        """
        raise NotImplementedError()

    # -- methods to inherent
    def _to_weekday(self, weekday_int: int) -> str:
        """ The user must make sure that 1 <= weekday_int <= 7
        """
        weekdays = {
            1: "Mon",
            2: "Tue",
            3: "Wed",
            4: "Thr",
            5: "Fri",
            6: "Sat",
            7: "Sun",
        }
        return weekdays[weekday_int]


class TimeTableNCTU(TimetableInterface):
    def __init__(self):
        self.__timespan_dic = {
            "M": "6:00-6:50",
            "N": "7:00-7:50",
            "A": "8:00-8:50",
            "B": "9:00-9:50",
            "C": "10:10-11:00",
            "D": "11:10-12:00",
            "X": "12:20-13:10",
            "E": "13:20-14:10",
            "F": "14:20-15:10",
            "G": "15:30-16:20",
            "H": "16:30-17:20",
            "Y": "17:30-18:20",
            "I": "18:30-19:20",
            "J": "19:30-20:20",
            "K": "20:30-21:20",
            "L": "21:30-22:20",
        }
        self.kind = "nctu"

    # -- Implementation of abstract methods
    def gen_timeslot(self, code: str, weekday_int: int) -> TimeSlot:
        if code.upper() not in self.__timespan_dic:
            raise Exception(f"not valid codename:{code}")
        if not (1 <= weekday_int <= 7):
            # Comparison chainning
            # https://docs.python.org/3/reference/expressions.html#comparisons
            raise Exception(f"not valid weekday:{weekday_int}")
        return TimeSlot(
            code=code.upper(),
            weekday=self._to_weekday(weekday_int),
            timespan=self.__timespan_dic[code],
            kind=self.kind,
        )

    def get_kind(self) -> str:
        return self.kind

    def is_valid_code(self, code) -> bool:
        return code.upper() in self.__timespan_dic

    def get_valid_codes(self) -> List[str]:
        return list(self.__timespan_dic.keys())

    ## -- private methods
    def __code2timespan(self, code: str) -> str:
        return self.__timespan_dic[code.upper()]
