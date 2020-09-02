from .timeslot_parser import TimeSlotParseException, TimeSlotParserNCTU
from .timetable import TimeTableNCTU

timetable_nctu = TimeTableNCTU()
time_slot_parser_nctu = TimeSlotParserNCTU(timetable_nctu)

__all__ = [
    # Time slot
    "time_slot_parser_nctu",
    "TimeSlotParseException",
]
