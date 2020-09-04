import re
from typing import List

from .objects import CodedTimeInterval
from .timetable import TimetableInterface


class TimeIntervalConvertException(Exception):
    pass


class TimeIntervalConverterInterface:
    """Convert specific timeslot encoding into CodedTimeInterval
    This Converter only do one thing:
        Use on a specific instance of TimetableInterface parse encoded timeslot string
        into a list of CodedTimeIntervals.
    Whether the timetable could be injected from the constructor of the child class
    """

    def to_time_intervals(self, s: str) -> List[CodedTimeInterval]:
        raise NotImplementedError()


class TimeIntervalConverterNCTU(TimeIntervalConverterInterface):
    def __init__(self, timetable: TimetableInterface):
        self.__timetable = timetable

        # NCTU styled course time encoding:
        #   e.g. 2A5CD, 1EF2G, 1AB
        #
        #   explanation:
        #       2A : the A timeslot in the Tuesday
        #       5CD : the C and D timeslots in the Friday
        self.__valid_encoding = re.compile(r"^(\d[A-Z]+)+$")
        self.__daily_schedule = re.compile(r"(\d)([A-Z]+)")

    # -- Implementation of abstract methods

    def to_time_intervals(self, s: str) -> List[CodedTimeInterval]:
        """ Break a encoded string into timeintervals
            e.g. "2A5CD" ->  ['2A', '5C', '5D']

            The user must ensure that :
                1. the input string must be encoded in valid format.
                2. the input string only contains uppercase and digit
            This method would raise TimeIntervalParseException if the user don't
                comply with the condiiton above.
        """
        if self.__valid_encoding.match(s) == None:
            raise TimeIntervalConvertException
        if s.upper() != s:
            raise TimeIntervalConvertException
        daily_schedule = self.__daily_schedule.findall(s)
        result = {}
        for weekday, timeslots in daily_schedule:
            for t in timeslots:
                key = f"{weekday}{t}"
                if key not in result:
                    result[key] = self.__timetable.gen_time_interval(
                        code=t, weekday_int=int(weekday)
                    )
        return list(result.values())
