from datetime import date

from pydantic import BaseModel


class Hobby(BaseModel):
    name: str
    since: date
