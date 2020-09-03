from typing import Dict, List

from app.models.course_timeslot import TimeSlotKind
from app.schemas import TimeSlotExp
from .timeslot_converter import TimeSlotConverterInterface
from .timetable import TimeSlot


class TimeSlotParseException(Exception):
    pass


class TimeSlotParserInterface:
    """A TimeSlotParser is able to parse different timeslot expressions
    into a list of timeslots.
        The implementation should utilize TimeSlotConveters under the hood.
    """

    def parse_timeslots(self, exp: TimeSlotExp) -> List[TimeSlot]:
        raise NotImplementedError()


class TimeSlotParser(TimeSlotParserInterface):
    def __init__(self, converters_map: Dict[TimeSlotKind, TimeSlotConverterInterface]):
        self.converters = converters_map

    def parse_timeslots(self, exp: TimeSlotExp) -> List[TimeSlot]:
        converter = self.converters[exp.kind]
        if not converter:
            raise TimeSlotParseException()
        return converter.to_time_slots(exp.value)
