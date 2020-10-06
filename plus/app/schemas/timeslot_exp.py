import re

from pydantic import BaseModel, Field, ValidationError, validator

from ..models.course_timeslot import TimeSlotKind


class TimeSlotExp(BaseModel):

    kind: TimeSlotKind = Field(example=TimeSlotKind.nctu)
    value: str = Field(example="2EF5G")

    @classmethod
    def get_example(cls):
        # There's a bug for FastAPI to render nested example by default Field() method, so we defined it here
        return TimeSlotExp(kind=TimeSlotKind.nctu, value="3EF5G")

    @validator("value")
    def number_and_code(cls, v, values):  # noqa
        # Parse and validate the format based on the input provided
        kind = values.get("kind", None)
        if kind == TimeSlotKind.nctu:
            # example: 3EF2G, 1A3CD
            res = re.match(r"^(\d[A-Za-z]+)+$", v)
            if not res:
                raise ValidationError(v)
            return v
        else:
            raise ValidationError(f"Not recognized encoding type: {kind}")
