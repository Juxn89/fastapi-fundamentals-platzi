from sqlmodel import select
from fastapi import APIRouter, status, HTTPException, Query

from db import SessionDep
from src.models.Customer import Customer
from src.models.Transaction import Transaction, TransactionCreate

router = APIRouter()

@router.post('/transactions', tags=["transactions"])
async def create_transaction(transaction_data: TransactionCreate, session: SessionDep):
    trans_data_dict = transaction_data.model_dump()
    customer = session.get(Customer, trans_data_dict.get('customer_id'))
    if not customer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer does not exits")
    transaction_db = Transaction.model_validate(trans_data_dict)
    session.add(transaction_db)
    session.commit()
    session.refresh(transaction_db)
    return transaction_db

@router.get('/transactions', status_code=status.HTTP_201_CREATED, tags=["transactions"])
async def list_transactions(
    session: SessionDep,
    skip: int = Query(0, description="Skip records"), 
    limit: int = Query(10, description="Total records limit") 
):
    query = select(Transaction).offset(skip).limit(limit)
    transactions = session.exec(query).all()
    return transactions