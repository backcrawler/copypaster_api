from typing import List, Optional

from pydantic.schema import BaseModel, datetime


class MyBase(BaseModel):
    '''ORM added by default'''
    class Config:
        orm_mode = True


class PasteName(MyBase):
    '''Response with the given name for a paste'''
    name: str


class PasteBase(MyBase):
    '''Base schema for a Paste data'''
    content: str
    expires: datetime
    groups: Optional[str][List[str]] = None


class OnePasteLoaded(PasteBase):
    '''A single paste loaded to the server'''
    pass


class OnePaste(PasteBase):
    '''Full paste fetched from DB'''
    name: str


class ManyPastes(MyBase):
    '''Multiple pastes fetched from DB'''
    data: List[OnePaste]
