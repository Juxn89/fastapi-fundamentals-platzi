import zoneinfo
from fastapi import FastAPI, HTTPException
from datetime import date, datetime

from src.models.Customer import Customer, CustomerCreate
from src.models.Invoice import Invoice
from src.models.Transaction import Transaction

app = FastAPI()

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
async def create_customer(customer_data: CustomerCreate):
    customer = Customer.model_validate(customer_data.model_dump())
    customer.id = len(DB_CUSTOMER)
    DB_CUSTOMER.append(customer)
    return customer

@app.get('/customers', response_model=list[Customer])
async def list_customers():
    return DB_CUSTOMER

@app.get('/customers/{customer_id}', response_model=Customer)
async def list_customers(customer_id: int):
    if customer_id < 0 or customer_id >= len(DB_CUSTOMER):
        raise HTTPException(status_code=404, detail="Customer not found")
    return DB_CUSTOMER[customer_id]

@app.post('/transactions')
async def create_transaction(transaction_data: Transaction):
    return transaction_data

@app.post('/invoices')
async def create_invoice(invoice_data: Invoice):
    return invoice_data