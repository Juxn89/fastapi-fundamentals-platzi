from pydantic import BaseModel
from sqlmodel import SQLModel, Field, Relationship

from src.models.Customer import Customer

class TransactionBase(SQLModel):
    ammount: int
    descriprion: str

class Transaction(TransactionBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    customer_id: int = Field(foreign_key="customer.id")
    customer: Customer = Relationship(back_populates="transactions")

class TransactionCreate(TransactionBase):
    customer_id: int = Field(foreign_key="customer.id")