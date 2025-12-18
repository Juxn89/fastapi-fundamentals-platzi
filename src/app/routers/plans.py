from sqlmodel import select
from fastapi import APIRouter, status, HTTPException

from db import SessionDep
from src.models.Plan import Plan

router = APIRouter()

@router.post("/plans", status_code=status.HTTP_201_CREATED, tags=["plans"])
def create_plan(plan_data: Plan, session: SessionDep):
    plan_db = Plan.model_validate(plan_data.model.dump())
    session.add(plan_db)
    session.commit()
    session.refresh(plan_data)
    return plan_db

@router.get("/plans", response_model=list[Plan], tags=["plans"])
def list_plan(session: SessionDep):
    plans = session.exec(select(Plan)).all()
    return plans