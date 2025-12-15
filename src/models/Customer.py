from pydantic import BaseModel, EmailStr

class CustomerBase(BaseModel):
    name: str
    description: str | None
    email: EmailStr
    age: int
    
class CustomerCreate(CustomerBase):
    pass 
   
class Customer(CustomerBase):
    id: int | None = None