from typing import Literal

from pydantic import BaseModel, Field, root_validator, ValidationError


class FormCreation(BaseModel):
    name: str = Field(...)

    class Config:
        extra = 'allow'

    @root_validator  # type: ignore
    def check_extra_fields(cls, values):
        valid_values = {'email', 'phone', 'date', 'text'}
        for field, value in values.items():
            if field != 'name' and value not in valid_values:
                raise ValidationError([
                    {
                        'loc': (field,),
                        'msg': (f'Field has invalid value {value}, '
                                f'must be one of {valid_values}')
                    }
                ])
        return values


class FormRecognizer(BaseModel):
    pass
