import zoneinfo
from sqlmodel import select
from datetime import date, datetime
from fastapi import FastAPI, HTTPException, status

from src.models.Invoice import Invoice
from db import SessionDep, create_all_table
from src.models.Transaction import Transaction
from src.models.Customer import Customer, CustomerCreate, CustomerUpdate

app = FastAPI(lifespan=create_all_table)

@app.get('/')
async def root():
    return { "message": "Hello world! Juan" }

@app.get('/current-time')
async def get_datetime():
    currentDate = date.today()
    currentTime = datetime.now().time()
    datetimeDetail = {
        "date": currentDate,
        "time": currentTime
        }
    return { 'datetime': datetimeDetail }

COUNTRY_ZONES = {
    "NI": "America/Managua",              # Nicaragua
    "CO": "America/Bogota",               # Colombia
    "MX": "America/Mexico_City",          # México
    "AR": "America/Argentina/Buenos_Aires", # Argentina
    "PE": "America/Lima",                 # Perú
    "US": "America/New_York",             # Estados Unidos
    "ES": "Europe/Madrid",                # España
    "JP": "Asia/Tokyo",                   # Japón
    "AU": "Australia/Sydney",             # Australia
    "BR": "America/Sao_Paulo"             # Brasil
}

@app.get('/current-time/{iso_code}')
async def get_current_time_isocode(iso_code: str):
    iso = iso_code.upper()
    timezone_str = COUNTRY_ZONES.get(iso)
    if not timezone_str:
        return { "message": "Timezone does not exist." }
    
    try:
        timezone = zoneinfo.ZoneInfo(timezone_str)
    except:
        return { "message": "Something was wrong. We don't recognize the ISO code or currently is not available." }
    return { iso_code: datetime.date(timezone) }

DB_CUSTOMER: list[Customer] = []
@app.post('/customers', response_model=Customer)
async def create_customer(customer_data: CustomerCreate, session: SessionDep):
    customer = Customer.model_validate(customer_data.model_dump())
    session.add(customer)
    session.commit()
    session.refresh(customer)
    return customer

@app.get('/customers', response_model=list[Customer])
async def list_customers(session: SessionDep):    
    return session.exec(select(Customer)).all()

@app.get('/customers/{customer_id}', response_model=Customer)
async def list_customers(customer_id: int, session: SessionDep):
    customer_db = session.get(Customer, customer_id)
    if not customer_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer does not exist.")
    return customer_db

@app.delete('/customers/{customer_id}')
async def delete_customers(customer_id: int, session: SessionDep):
    customer_db = session.get(Customer, customer_id)
    if not customer_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer does not exist.")
    session.delete(customer_db)
    session.commit()
    return { "detail" : "OK"}

@app.patch('/customers/{customer_id}', response_model=Customer, status_code=status.HTTP_201_CREATED)
async def list_customers(customer_id: int, customer_data: CustomerUpdate, session: SessionDep):
    customer_db = session.get(Customer, customer_id)
    if not customer_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer does not exist.")
    customer_data_dict = customer_data.model_dump(exclude_unset=True)
    customer_db.sqlmodel_update(customer_data_dict)
    session.add(customer_db)
    session.commit()
    session.refresh(customer_db)
    return customer_db

@app.post('/transactions')
async def create_transaction(transaction_data: Transaction):
    return transaction_data

@app.post('/invoices')
async def create_invoice(invoice_data: Invoice):
    return invoice_data