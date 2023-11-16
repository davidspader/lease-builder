from app.schemas.base import CustomBaseModel
from pydantic import field_validator

class Template(CustomBaseModel):
    id: str
    description: str

    @field_validator('description')
    def validate_name(cls, value):
        if len(value) == 0:
            raise ValueError("empty description not allowed")
        return value