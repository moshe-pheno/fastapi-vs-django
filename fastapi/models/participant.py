from pydantic import BaseModel

from models.hobby import Hobby


class Participant(BaseModel):
    name: str
    age: int
    hobbies: list[Hobby]
