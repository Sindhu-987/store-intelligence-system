import pytest

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.database import Base


SQLALCHEMY_DATABASE_URL = (
    "sqlite:///:memory:"
)

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={
        "check_same_thread": False
    }
)

TestingSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


@pytest.fixture
def db():

    Base.metadata.create_all(
        bind=engine
    )

    session = TestingSessionLocal()

    yield session

    session.close()

    Base.metadata.drop_all(
        bind=engine
    )