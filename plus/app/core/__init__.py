from ..models.course_timeslot import TimeSlotKind
from .timeslot_converter import TimeSlotConverterNCTU, TimeSlotConvertException
from .timeslot_parser import TimeSlotParseException, TimeSlotParser
from .timetable import TimeTableNCTU

# Parser
converters_map = {TimeSlotKind.nctu: TimeSlotConverterNCTU(TimeTableNCTU())}
timeslot_parser = TimeSlotParser(converters_map=converters_map)


__all__ = [
    "timeslot_parser",
    "TimeSlotParseException",
    "TimeSlotConvertException",
]
