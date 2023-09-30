from datetime import datetime
from typing import Optional

from app.services.constants import MIN_STRING, MAX_STRING
from pydantic import BaseModel, Extra, Field, PositiveInt


class CharityProjectBase(BaseModel):
    name: str
    description: str
    full_amount: PositiveInt

    class Config:
        extra = Extra.forbid
        BaseModel.Config.min_anystr_length = MIN_STRING


class CharityProjectCreate(CharityProjectBase):
    name: str = Field(..., max_length=MAX_STRING)
    description: str = Field(...,)


class CharityProjectUpdate(BaseModel):
    name: Optional[str] = Field(None)
    description: Optional[str] = Field(None)
    full_amount: Optional[PositiveInt]

    class Config:
        extra = Extra.forbid


class CharityProjectDB(CharityProjectBase):
    id: int
    invested_amount: int
    fully_invested: bool
    create_date: datetime
    close_date: Optional[datetime]

    class Config:
        orm_mode = True
