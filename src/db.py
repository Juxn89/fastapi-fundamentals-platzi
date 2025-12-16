from typing import Annotated
from fastapi import Depends, FastAPI
from sqlmodel import Session, create_engine, SQLModel
from contextlib import asynccontextmanager

SQLITE_NAME = 'db.sqlite3'
SQLITE_URL = f"sqlite:///{SQLITE_NAME}"

CURRENT_ENGINE = create_engine(SQLITE_URL)

@asynccontextmanager
async def create_all_table(app: FastAPI):
    SQLModel.metadata.create_all(CURRENT_ENGINE)
    yield

def get_session():
    with Session(CURRENT_ENGINE) as session:
        yield session
        
SessionDep = Annotated[Session, Depends(get_session)]