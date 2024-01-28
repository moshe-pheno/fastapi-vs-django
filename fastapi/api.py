from datetime import date
from typing import Iterable

from fastapi import FastAPI

from models.hobby import Hobby
from models.participant import Participant

app = FastAPI()

robert = Participant(name='Robert', age=30, hobbies=[
    Hobby(name='painting', since=date.fromisoformat('2019-04-01')),
    Hobby(name='running', since=date.fromisoformat('2022-05-02'))
])

participants = [robert]


@app.get('participants')
def list_participants(amount: int = 5) -> Iterable[Participant]:
    return participants[:amount]


@app.post('participant')
def create_participant(details: Participant) -> Participant:
    participants.append(details)
    return details
