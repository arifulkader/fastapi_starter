from typing import Optional
from pydantic import BaseModel


class StaffBase(BaseModel):
    username: str
    email: Optional[str]


class StaffCreate(StaffBase):
    password: str


class StaffRes(StaffBase):
    id: int
    is_active: str

    class Config:
        from_attributes = True
    