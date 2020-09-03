import attr

from ..models.course_timeslot import TimeSlotKind

# TODO: move TimeslotKind from models to here


@attr.s(auto_attribs=True, frozen=True)
class CodedTimeInterval:
    """ Represent a single timeslot interval used between courses,
    which is defined by different timetables.
    This object is used for internal communication, so it is immutable
    by default.
    This class support comparison by default.
    """

    # TODO: add validation for `timespan` and `kind`

    code: str
    weekday: str
    timespan: str
    kind: TimeSlotKind

    def as_dict(self):
        """ Return this object as a dictionary
        """
        return attr.asdict(self)

    def evlove(self, **changes):
        """ Create a new instance, based on this obejct with changes applied.
        """
        return attr.evolve(self, **changes)
