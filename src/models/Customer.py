from pydantic import EmailStr, field_validator
from sqlmodel import SQLModel, Field, Relationship, Session, select
from db import CURRENT_ENGINE

from src.models.Plan import CustomerPlan

class CustomerBase(SQLModel):
    name: str = Field(default=None)
    description: str | None = Field(default=None)
    email: EmailStr = Field(default=None)
    age: int = Field(default=None)
    @field_validator("email")
    def validate_email(cls, value):
        session = Session(CURRENT_ENGINE)
        query = select(Customer).where(Customer.email == value)
        result = session.exec(query).first()
        if result:
            raise ValueError("This email is already registered")
        return value
    
class CustomerCreate(CustomerBase):
    pass 
    
class CustomerUpdate(CustomerBase):
    pass 
   
class Customer(CustomerBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    transactions: list["Transaction"] = Relationship(back_populates="customer")
    plans: list["Plan"] = Relationship(
        back_populates="customers",
        link_model=CustomerPlan
    )