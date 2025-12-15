from pydantic import BaseModel
from src.models.Customer import Customer
from src.models.Transaction import Transaction

class Invoice(BaseModel):
   id: int
   customer: Customer
   transactions: list[Transaction]
   total: int
   @property
   def ammount_total(self):
      return sum(transaction.ammount for transaction in self.transactions)
