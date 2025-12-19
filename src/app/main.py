import time
import zoneinfo
from typing import Annotated
from datetime import date, datetime
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi import FastAPI, Request, Depends, HTTPException, status

from db import create_all_table
from src.models.Invoice import Invoice
from src.app.routers import customers, transactions, plans

app = FastAPI(lifespan=create_all_table)
app.include_router(customers.router)
app.include_router(transactions.router)
app.include_router(plans.router)

@app.middleware("http")
async def log_request_time(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    print(f"Request: {request.url} completed in: {process_time:.4f} seconds")
    return response

@app.middleware("http")
async def log_request_headers(request: Request, call_next) -> Request:
    print(f"Request headers: {request.headers}")
    response = await call_next(request)
    return response

securiry = HTTPBasic()
@app.get('/')
async def root(credentials: Annotated[HTTPBasicCredentials, Depends(securiry)]):
    print(credentials)
    if credentials.username == "" and credentials.password == "":
    	return { "message": f"Hello world! {credentials.username}" }
    else:
      raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

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

@app.post('/invoices')
async def create_invoice(invoice_data: Invoice):
    return invoice_data