from sqlmodel import select
from fastapi import APIRouter, status, HTTPException, Query

from src.db import SessionDep
from src.models.Plan import Plan, CustomerPlan, StatusEnum
from src.models.Customer import Customer, CustomerCreate, CustomerUpdate

router = APIRouter()

@router.post('/customers', response_model=Customer, tags=['customers'])
async def create_customer(customer_data: CustomerCreate, session: SessionDep):
    customer = Customer.model_validate(customer_data.model_dump())
    session.add(customer)
    session.commit()
    session.refresh(customer)
    return customer

@router.get('/customers', response_model=list[Customer], tags=['customers'])
async def list_customers(session: SessionDep):    
    return session.exec(select(Customer)).all()

@router.get('/customers/{customer_id}', response_model=Customer, tags=['customers'])
async def list_customers(customer_id: int, session: SessionDep):
    customer_db = session.get(Customer, customer_id)
    if not customer_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer does not exist.")
    return customer_db

@router.delete('/customers/{customer_id}', tags=['customers'])
async def delete_customers(customer_id: int, session: SessionDep):
    customer_db = session.get(Customer, customer_id)
    if not customer_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer does not exist.")
    session.delete(customer_db)
    session.commit()
    return { "detail" : "OK"}

@router.patch('/customers/{customer_id}', response_model=Customer, status_code=status.HTTP_201_CREATED, tags=['customers'])
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

@router.post("/customer/{customer_id}/{plan_id}", tags=["customers"])
async def subscribe_customer_to_plan(customer_id: int, plan_id: int, session: SessionDep, plan_status: StatusEnum = Query()):
    customer_db = session.get(Customer, customer_id)
    plan_db = session.get(Plan, plan_id)
    if not customer_db or not plan_db:
    	raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="The customer or plan does not exit.")
    customer_plan_db = CustomerPlan(plan_id=plan_db.id, customer_id=customer_db.id, status=plan_status )
    session.add(customer_plan_db)
    session.commit()
    session.refresh(customer_plan_db)
    return customer_plan_db
    
@router.get("/customer/{customer_id}", tags=["customers"])
async def subscribe_customer_to_plan(customer_id: int, session: SessionDep, plant_status: StatusEnum = Query()):
    customer_db = session.get(Customer, customer_id)
    if not customer_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="The customer does not exit.")
    query = (
         select(CustomerPlan)
        .where(CustomerPlan.customer_id == customer_id)
        .where(CustomerPlan.status == plant_status)
    )
    plan = ssession.exec(query).all()
    return plans