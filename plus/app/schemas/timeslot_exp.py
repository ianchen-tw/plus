import re

from pydantic import BaseModel, ValidationError, validator

from ..models.course_timeslot import TimeSlotKind


class TimeSlotExp(BaseModel):

    kind: TimeSlotKind
    value: str

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

    # Provide example for openapi
    class Config:
        schema_extra = {"example": {"kind": "nctu", "value": "2EF5G",}}
