import pytest
from sqlmodel import SQLModel, Session
from sqlalchemy.pool import StaticPool
from sqlalchemy import create_engine
from fastapi.testclient import TestClient

from src.db import get_session
from src.app.main import app

sqlite_name = "db.sqlite3"
sqlite_url = f"sqlite:///{sqlite_name}"

ENGINE = create_engine(sqlite_url, connect_args={"check_same_thread": False}, poolclass=StaticPool)

@pytest.fixture(name="session")
def session_fixture():
    SQLModel.metadata.create_all(ENGINE)
    with Session(ENGINE) as session:
        yield session
    SQLModel.metadata.drop_all(ENGINE)
    
@pytest.fixture(name="client")
def client_fixture(session: Session):
    def get_session_override():
        return session
    app.dependency_overrides[get_session] = get_session_override
    client = TestClient(app)
    yield client
    app.dependency_overrides.clear()