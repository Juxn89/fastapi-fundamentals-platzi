from pydantic import BaseModel

class Transaction(BaseModel):
    id: int
    ammount: int
    descriprion: str