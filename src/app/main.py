import zoneinfo
from fastapi import FastAPI
from datetime import date, datetime

from db import create_all_table
from src.models.Invoice import Invoice
from src.models.Customer import Customer
from src.models.Transaction import Transaction
from src.app.routers import customers

app = FastAPI(lifespan=create_all_table)
app.include_router(customers.router)

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


@app.post('/transactions')
async def create_transaction(transaction_data: Transaction):
    return transaction_data

@app.post('/invoices')
async def create_invoice(invoice_data: Invoice):
    return invoice_data