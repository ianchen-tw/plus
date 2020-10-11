from typing import Dict, List

from app.models.course_timeslot import TimeSlotKind
from app.schemas import TimeSlotExp
from .objects import CodedTimeInterval
from .time_interval_converter import TimeIntervalConverterInterface


class TimeIntervalParseException(Exception):
    pass


class TimeIntervalParserInterface:
    """A TimeIntervalParser is able to parse different time_interval expressions
    into a list of time_interval.
        The implementation should utilize TimeIntervalConveters under the hood.
    """

    def parse_time_intervals(self, exp: TimeSlotExp) -> List[CodedTimeInterval]:
        raise NotImplementedError()


class TimeIntervalParser(TimeIntervalParserInterface):
    def __init__(
        self, converters_map: Dict[TimeSlotKind, TimeIntervalConverterInterface]
    ):
        self.converters = converters_map

    def parse_time_intervals(self, exp: TimeSlotExp) -> List[CodedTimeInterval]:
        converter = self.converters[exp.kind]
        if not converter:
            raise TimeIntervalParseException()
        return converter.to_time_intervals(exp.value)
