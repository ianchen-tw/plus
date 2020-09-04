from ..models.course_timeslot import TimeSlotKind
from .time_interval_converter import (
    TimeIntervalConverterNCTU,
    TimeIntervalConvertException,
)
from .time_interval_parser import TimeIntervalParseException, TimeIntervalParser
from .timetable import TimeTableNCTU

# Parser
converters_map = {TimeSlotKind.nctu: TimeIntervalConverterNCTU(TimeTableNCTU())}
time_interval_parser = TimeIntervalParser(converters_map=converters_map)


__all__ = [
    "time_interval_parser",
    "TimeIntervalParseException",
    "TimeIntervalConvertException",
]
